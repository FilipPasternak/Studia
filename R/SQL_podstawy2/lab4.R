# NIE EDYTOWAĆ *****************************************************************
dsn_database = "wbauer_adb_2023"   # Specify the name of  Database
dsn_hostname = "pgsql-196447.vipserv.org"  # Specify host name 
dsn_port = "5432"                # Specify your port number. 
dsn_uid = "wbauer_adb"         # Specify your username. 
dsn_pwd = "adb2020"        # Specify your password.

library(DBI)
library(RPostgres)
library(testthat)

con <- dbConnect(Postgres(), dbname = dsn_database, host=dsn_hostname, port=dsn_port, user=dsn_uid, password=dsn_pwd) 
# ******************************************************************************

film_in_category<- function(category_id)
{
  # Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego id kategorii.
  # Przykład wynikowej tabeli:
  # |   |title          |language    |category|
  # |0	|Amadeus Holy	|English	|Action|
  # 
  # Tabela wynikowa ma być posortowana po tylule filmu i języku.
  # 
  # Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość NULL
  # 
  # Parameters:
  # category_id (integer): wartość id kategorii dla którego wykonujemy zapytanie
  # 
  # Returns:
  # DataFrame: DataFrame zawierający wyniki zapytania
  # 
  
  if (category_id %in% dbGetQuery(con, "SELECT category_id FROM category")$category_id & is.numeric(category_id)){
  
    query <- paste("SELECT film.title, lang.name, category.name FROM film_category AS fc
              JOIN category ON category.category_id = fc.category_id
              JOIN film ON fc.film_id = film.film_id
              JOIN language AS lang ON lang.language_id = film.language_id
              WHERE category.category_id =", category_id, "
              ORDER BY film.title")
    df <- dbGetQuery(con, query)
    
    return(df)
  }
  else{
    return(NULL)
  }
}


number_films_in_category <- function(category_id){
  #   Funkcja zwracająca wynik zapytania do bazy o ilość filmów w zadanej kategori przez id kategorii.
  #     Przykład wynikowej tabeli:
  #     |   |category   |count|
  #     |0	|Action 	|64	  | 
  #     
  #     Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość NULL.
  #         
  #     Parameters:
  #     category_id (integer): wartość id kategorii dla którego wykonujemy zapytanie
  #     
  #     Returns:
  #     DataFrame: DataFrame zawierający wyniki zapytania
  
  if (category_id %in% dbGetQuery(con, "SELECT category_id FROM category")$category_id & is.numeric(category_id)){
  
    df <- film_in_category(category_id)
    
    number_of_films = length(df$title)
    
    query <- paste("SELECT category.name AS category,", number_of_films, " AS count FROM category
                   WHERE category.category_id =", category_id)
    return(dbGetQuery(con, query))
    
  }
  else {
    return(NULL)
  }
}



number_film_by_length <- function(min_length, max_length){
  #   Funkcja zwracająca wynik zapytania do bazy o ilość filmów dla poszczegulnych długości pomiędzy wartościami min_length a max_length.
  #     Przykład wynikowej tabeli:
  #     |   |length     |count|
  #     |0	|46 	    |64	  | 
  #     
  #     Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość NULL.
  #         
  #     Parameters:
  #     min_length (int,double): wartość minimalnej długości filmu
  #     max_length (int,double): wartość maksymalnej długości filmu
  #     
  #     Returns:
  #     pd.DataFrame: DataFrame zawierający wyniki zapytania
  
  if (!is.numeric(min_length) || !is.numeric(max_length)){
    return(NULL)
  }
  
  if (min_length > max_length){
    return(NULL)
  }
  else{
    l = max_length - min_length
    
    query <- paste("SELECT film.title FROM film
                   WHERE ", min_length, " < film.length AND film.length < ", max_length)
    df <- dbGetQuery(con, query)
    
    number_of_films <- length(df$title)
    
    query_final <- paste("SELECT ", l, " AS length, ", number_of_films, " AS count")
    
    return(dbGetQuery(con, query_final))
    
  }
  
  
  return(NULL)
}


client_from_city<- function(city){
  #   Funkcja zwracająca wynik zapytania do bazy o listę klientów z zadanego miasta przez wartość city.
  #     Przykład wynikowej tabeli:
  #     |   |city	    |first_name	|last_name
  #     |0	|Athenai	|Linda	    |Williams
  #     
  #     Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
  #     
  #     Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość NULL.
  #         
  #     Parameters:
  #     city (character): nazwa miaste dla którego mamy sporządzić listę klientów
  #     
  #     Returns:
  #     DataFrame: DataFrame zawierający wyniki zapytania
  
  if (city %in% dbGetQuery(con, "SELECT city.city FROM city")$city & is.character(city)){
    
    query <- paste("SELECT c.city, cs.first_name, cs.last_name FROM city AS c
                   JOIN address AS adr ON adr.city_id = c.city_id
                   JOIN customer AS cs ON cs.address_id = adr.address_id
                   WHERE c.city_id = ", city)
    return(dbGetQuery(con, query))
  }
  else{
    return(NULL)
  }
}

avg_amount_by_length<-function(length){
  #   Funkcja zwracająca wynik zapytania do bazy o średnią wartość wypożyczenia filmów dla zadanej długości length.
  #     Przykład wynikowej tabeli:
  #     |   |length |avg
  #     |0	|48	    |4.295389
  #     
  #     
  #     Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość NULL.
  #         
  #     Parameters:
  #     length (integer,double): długość filmu dla którego mamy pożyczyć średnią wartość wypożyczonych filmów
  #     
  #     Returns:
  #     DataFrame: DataFrame zawierający wyniki zapytania
  
  if(length > 0 & is.numeric(length)){
    
    query <- paste("SELECT p.amount FROM film AS f
                   JOIN inventory AS inv ON inv.film_id = f.film_id
                   JOIN rental AS r ON r.inventory_id = inv.inventory_id
                   JOIN payment AS p ON p.rental_id = r.rental_id
                   WHERE f.length = ", length)
    df <- dbGetQuery(con, query)
    
    if (nrow(df) > 0){
      average_payment <- mean(df$amount)
      result_df <- data.frame(length = length, avg = average_payment)
      return(result_df)
      } 
  }
  else{
    return(NULL)
  }
}



client_by_sum_length<-function(sum_min){
  #   Funkcja zwracająca wynik zapytania do bazy o sumaryczny czas wypożyczonych filmów przez klientów powyżej zadanej wartości .
  #     Przykład wynikowej tabeli:
  #     |   |first_name |last_name  |sum
  #     |0  |Brian	    |Wyman  	|1265
  #     
  #     Tabela wynikowa powinna być posortowane według sumy, imienia i nazwiska klienta.
  #     Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość NULL.
  #         
  #     Parameters:
  #     sum_min (integer,double): minimalna wartość sumy długości wypożyczonych filmów którą musi spełniać klient
  #     
  #     Returns:
  #     DataFrame: DataFrame zawierający wyniki zapytania
  
  if(is.numeric(sum_min) & sum_min > 0){
    
    query <- paste("SELECT c.first_name, c.last_name, SUM(f.length) AS sum FROM customer as c
                   JOIN rental AS r ON c.customer_id = r.customer_id
                   JOIN inventory AS inv ON r.inventory_id = inv.inventory_id
                   JOIN film AS f ON inv.film_id = inv.film_id
                   GROUP BY c.first_name, c.last_name
                   HAVING SUM(f.length) > ", sum_min, "
                   ORDER BY sum, c.first_name, c.last_name")
    
    return(dbGetQuery(con, query))
    
  }
  else{
    return(NULL)
  }
}


category_statistic_length<-function(name){
  #   Funkcja zwracająca wynik zapytania do bazy o statystykę długości filmów w kategorii o zadanej nazwie.
  #     Przykład wynikowej tabeli:
  #     |   |category   |avg    |sum    |min    |max
  #     |0	|Action 	|111.60 |7143   |47 	|185
  #     
  #     Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość NULL.
  #         
  #     Parameters:
  #     name (character): Nazwa kategorii dla której ma zostać wypisana statystyka
  #     
  #     Returns:
  #     DataFrame: DataFrame zawierający wyniki zapytania
  
  if (is.character(name) & name %in% dbGetQuery(con, "SELECT c.name FROM category AS c")$name){
    
    query <- paste("SELECT c.name AS category, AVG(f.length) AS avg, SUM(f.length) AS sum, MIN(f.length) AS min, MAX(f.length) AS max FROM category AS c
                   JOIN film_category AS fc ON fc.category_id = c.category_id
                   JOIN film AS f ON f.film_id = fc.film_id
                   WHERE c.name = '", name, "'
                   GROUP BY c.name")
    
    return(dbGetQuery(con, query))
  }
  else{
    return(NULL)
  }
}


# NIE EDYTOWAĆ *****************************************************************
test_dir('tests/testthat')
# ******************************************************************************