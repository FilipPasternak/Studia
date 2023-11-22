library(DBI)
library(RPostgres)

dsn_database = "wbauer_adb_2023"   
dsn_hostname = "pgsql-196447.vipserv.org"  
dsn_port = "5432"                
dsn_uid = "wbauer_adb"        
dsn_pwd = "adb2020"  

con <- dbConnect(Postgres(), dbname = dsn_database, host=dsn_hostname, port=dsn_port, user=dsn_uid, password=dsn_pwd)

# Zadanie 1

query1 <- "SELECT DISTINCT name FROM category"
df1 <- dbGetQuery(con, query1)

Liczba_Kategorii <- length(df1$name)
print(Liczba_Kategorii)

# Zadanie 2

query2 <- "SELECT DISTINCT name FROM category
           ORDER BY name"
df2 <- dbGetQuery(con, query2)
print(df2)

# Zadanie 3

query3_a <- "SELECT release_year, title FROM film
           ORDER BY release_year"
df3_a <- dbGetQuery(con, query3_a)

query3_b <- "SELECT release_year, title FROM film
           ORDER BY release_year ASC"
df3_b <- dbGetQuery(con, query3_b)

Najstarszy <- df3_a$title[1]
Najmlodszy <- df3_b$title[1]
# Metoda działałaby poprawnie, gdyby filmy były z różnych lat

# Zadanie 4

query4 <- "SELECT rental_date FROM rental
           WHERE rental_date >= '2005-07-01' AND rental_date < '2005-08-01'"
df4 <- dbGetQuery(con, query4)

Liczba_Wyporzyczen1 <- length(df4$rental_date)

# Zadanie 5

query5 <- "SELECT rental_date FROM rental
           WHERE rental_date >= '2010-01-01' AND rental_date < '2011-02-01'"
df5 <- dbGetQuery(con, query5)

Liczba_Wyporzyczen2 <- length(df5$rental_date)

# Zadanie 6

query6 <- "SELECT amount FROM payment
           ORDER BY amount DESC"
df6 <- dbGetQuery(con, query6)

Najwyzsza_platnosc <- df6$amount[1]

# Zadanie 7

query7 <- "SELECT cy.country, c.first_name, c.last_name FROM customer AS c
           JOIN address AS a on c.address_id = a.address_id
           JOIN city AS ct ON a.city_id = ct.city_id
           JOIN country AS cy ON ct.country_id = cy.country_id"
           
df7 <- dbGetQuery(con, query7)

# Zadanie 8

query8 <- "SELECT DISTINCT cy.country, s.first_name, s.last_name FROM staff AS s
           JOIN address AS a on s.address_id = a.address_id
           JOIN city AS ct ON a.city_id = ct.city_id
           JOIN country AS cy ON ct.country_id = cy.country_id"
df8 <- dbGetQuery(con, query8)

# Zadanie 9

query9 <- "SELECT cy.country, s.first_name, s.last_name FROM staff AS s
           JOIN address AS a on s.address_id = a.address_id
           JOIN city AS ct ON a.city_id = ct.city_id
           JOIN country AS cy ON ct.country_id = cy.country_id
           WHERE cy.country IN ('Argentina', 'Spain')"

df9 <- dbGetQuery(con, query9)

number_of_employees <- length(df9$country)


# Zadanie 10

query10 <- "SELECT DISTINCT cat.name FROM rental AS rent
            JOIN inventory AS inv ON rent.inventory_id = inv.inventory_id
            JOIN film AS f ON inv.film_id = f.film_id
            JOIN film_category AS fc ON f.film_id = fc.film_id
            JOIN category AS cat ON fc.category_id = cat.category_id"

df10 <- dbGetQuery(con, query10)

# Zadanie 11

query11 <- "SELECT DISTINCT cat.name FROM rental AS rent
            JOIN inventory AS inv ON rent.inventory_id = inv.inventory_id
            JOIN film AS f ON inv.film_id = f.film_id
            JOIN film_category AS fc ON f.film_id = fc.film_id
            JOIN category AS cat ON fc.category_id = cat.category_id

            JOIN customer AS c ON c.customer_id = rent.customer_id
            JOIN address AS a on c.address_id = a.address_id
            JOIN city AS ct ON a.city_id = ct.city_id
            JOIN country AS cy ON ct.country_id = cy.country_id
            WHERE cy.country IN ('USA')"

df11 <- dbGetQuery(con, query11)

# Zadanie 12

query12 <- "SELECT f.title FROM film AS f
            JOIN film_actor AS fa ON f.film_id = fa.film_id
            JOIN actor AS a ON fa.actor_id = a.actor_id
            WHERE a.first_name IN ('Olympia', 'Julia', 'Ellen') AND a.last_name IN ('Pfeiffer', 'Zellweger', 'Presley')" 
 
df12 <- dbGetQuery(con, query12)