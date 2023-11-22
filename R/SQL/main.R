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

film_in_category <- function(category)
{
  # Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
  #     - id: jeżeli categry jest integer
  #     - name: jeżeli category jest character, dokładnie taki jak podana wartość
  # Przykład wynikowej tabeli:
  # |   |title          |languge    |category|
  # |0	|Amadeus Holy	|English	|Action|
  # 
  # Tabela wynikowa ma być posortowana po tylule filmu i języku.
  # 
  # Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość NULL.
  # 
  # Parameters:
  # category (integer,character): wartość kategorii po id (jeżeli typ integer) lub nazwie (jeżeli typ character)  dla którego wykonujemy zapytanie
  # 
  # Returns:
  # DataFrame: DataFrame zawierający wyniki zapytania
  
  if (is.integer(category)){
    
    query <- paste("SELECT film.title AS title, lang.name AS languge, category.name AS category FROM film_category AS fc
              JOIN category ON category.category_id = fc.category_id
              JOIN film ON fc.film_id = film.film_id
              JOIN language AS lang ON lang.language_id = film.language_id
              WHERE category.category_id =", category, "
              ORDER BY film.title, lang.name")
    df <- dbGetQuery(con, query)
    
    return(df)
  }
  
  if(is.character(category)){
    
    query <- paste("SELECT f.title AS title, l.name AS languge, c.name AS category FROM category AS c
                   JOIN film_category AS fc ON fc.category_id = c.category_id
                   JOIN film AS f ON f.film_id = fc.film_id
                   JOIN language AS l ON l.language_id = f.language_id
                   WHERE c.name = '", category, "'
                   ORDER BY f.title, l.name", sep = "")
    df <- dbGetQuery(con, query)
    
    return(df)
  }  
    
  else{
    return(NULL)
  }
}





film_in_category_case_insensitive <- function(category)
{
  #  Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
  #     - id: jeżeli categry jest integer
  #     - name: jeżeli category jest character
  #  Przykład wynikowej tabeli:
  #     |   |title          |languge    |category|
  #     |0	|Amadeus Holy	|English	|Action|
  #     
  #   Tabela wynikowa ma być posortowana po tylule filmu i języku.
  #     
  #     Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość NULL.
  
  #   Parameters:
  #   category (integer,str): wartość kategorii po id (jeżeli typ integer) lub nazwie (jeżeli typ character)  dla którego wykonujemy zapytanie
  #
  #   Returns:
  #   DataFrame: DataFrame zawierający wyniki zapytania
  
  if (is.integer(category)){
    
    query <- paste("SELECT film.title AS title, lang.name AS languge, category.name AS category FROM film_category AS fc
              JOIN category ON category.category_id = fc.category_id
              JOIN film ON fc.film_id = film.film_id
              JOIN language AS lang ON lang.language_id = film.language_id
              WHERE category.category_id =", category, "
              ORDER BY film.title, lang.name")
    df <- dbGetQuery(con, query)
    
    return(df)
  }
  
  if(is.character(category)){
    
    query <- paste("SELECT f.title AS title, l.name AS languge, c.name AS category FROM category AS c
                   JOIN film_category AS fc ON fc.category_id = c.category_id
                   JOIN film AS f ON f.film_id = fc.film_id
                   JOIN language AS l ON l.language_id = f.language_id
                   WHERE c.name ILIKE '", category, "'
                   ORDER BY f.title, l.name", sep = "")
    df <- dbGetQuery(con, query)
    
    return(df)
  }  
  
  else{
    return(NULL)
  }
}



film_cast <- function(title)
{
  # Funkcja zwracająca wynik zapytania do bazy o obsadę filmu o dokładnie zadanym tytule.
  # Przykład wynikowej tabeli:
  #     |   |first_name |last_name  |
  #     |0	|Greg       |Chaplin    | 
  #     
  # Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
  # Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość NULL.
  #         
  # Parameters:
  # title (character): wartość id kategorii dla którego wykonujemy zapytanie
  #     
  # Returns:
  # DataFrame: DataFrame zawierający wyniki zapytania
  
  if (is.character(title)){
    
    query <- paste("SELECT a.first_name, a.last_name FROM film AS f
                   JOIN film_actor AS fa ON fa.film_id = f.film_id
                   JOIN actor AS a ON fa.actor_id = a.actor_id
                   WHERE f.title ILIKE '", title, "'
                   ORDER BY a.last_name, a.first_name", sep = "")
    
    df <- dbGetQuery(con, query)
    
    return(df)
    
  }
  else{
    return(NULL)
  }
}




film_title_case_insensitive <- function(words)
{
  # Funkcja zwracająca wynik zapytania do bazy o tytuły filmów zawierających conajmniej jedno z podanych słów z listy words.
  # Przykład wynikowej tabeli:
  #     |   |title              |
  #     |0	|Crystal Breaking 	| 
  #     
  # Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
  # 
  # Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość NULL.
  #         
  # Parameters:
  # words(list[character]): wartość minimalnej długości filmu
  #     
  # Returns:
  # DataFrame: DataFrame zawierający wyniki zapytania
  # 
  
  if (is.vector(words) & all(sapply(words, is.character))){
    
    query <- "SELECT f.title AS title FROM film AS f
              WHERE f.title ~* "
    
    for(i in seq_len(length(words))){
      if(i < length(words)){
        query <- paste(query, "'\\y", words[i], "\\y' OR f.title ~* ",  sep = "")
      }
      else{
        query <- paste(query, "'\\y", words[i], "\\y'",  sep = "")
      }
    }
    query <- paste(query, "
                   ORDER BY f.title")
    print(query)  
    return(dbGetQuery(con, query))
  }
  
  else{
    return(NULL)
  }
  
}



# NIE EDYTOWAĆ *****************************************************************
test_dir('tests/testthat')
# ******************************************************************************