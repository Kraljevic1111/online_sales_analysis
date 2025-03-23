# online_sales_analysis
## Opis projekta
**Online Sales Analysis** je Python projekat koji omogućava upravljanje proizvodima, njihovu analizu i rad sa korpom kupaca. Projekat koristi klase za organizaciju proizvoda i upravljanje podacima o prodaji.

## Struktura projekta
Projekt se sastoji od sledećih glavnih Python datoteka:

- **product.py** – Definiše klasu `Product` za rad sa pojedinačnim proizvodima.
- **product_manager.py** – Sadrži klasu `ProductManager` koja omogućava upravljanje kolekcijom proizvoda.
- **cart.py** – Implementira klasu `Cart` za rad sa korpom kupaca.
- **main.py** – Glavna izvršna datoteka koja testira funkcionalnosti svih klasa.
- **.gitignore** – Sprečava verzionisanje poverljivih podataka i snimaka ekrana.

## Klase i funkcionalnosti

### 1. Klasa `Product`
Sadrži osnovne informacije o proizvodu:
- `name` – naziv proizvoda
- `price` – cena proizvoda
- `quantity` – količina proizvoda na lageru

Metodi:
- `display_info()` – vraća informacije o proizvodu.
- `update_quantity(new_quantity)` – ažurira količinu proizvoda.

### 2. Klasa `ProductManager`
Upravlja listom proizvoda:
- `products` – lista dostupnih proizvoda

Metodi:
- `add_product(product)` – dodaje novi proizvod u listu.
- `remove_product(product_name)` – uklanja proizvod iz liste prema imenu.
- `display_products()` – prikazuje sve proizvode.
- `total_inventory_value()` – računa ukupnu vrednost svih proizvoda na lageru.

### 3. Klasa `Cart`
Omogućava upravljanje korpom kupaca:
- `cart_items` – lista proizvoda u korpi

Metodi:
- `add_to_cart(product)` – dodaje proizvod u korpu.
- `total_cart_value()` – računa ukupnu vrednost proizvoda u korpi.
- `display_cart()` – prikazuje sve proizvode u korpi.

## Kako koristiti
1. Pokrenuti `main.py` kako bi se testirale funkcionalnosti.
2. Dodati proizvode u listu proizvoda pomoću `ProductManager` klase.
3. Kreirati instancu `Cart` i dodati proizvode u korpu.
4. Prikazati sadržaj korpe i izračunati ukupnu vrednost.

## Verzije i upravljanje granama
Tokom razvoja korišćene su sledeće grane:
- `main` – Glavna grana projekta.
- `add-product-removal` – Dodata mogućnost uklanjanja proizvoda.
- `add-cart-functionality` – Implementirana klasa `Cart` i dodata u projekat.

## .gitignore pravila
`.gitignore` je podešen da ignoriše:
- `config.json` – čuva poverljive podatke poput API ključeva i adresa baze podataka.
- Svi snimci ekrana (`*.png`, `*.jpg`, `*.jpeg`, `*.gif`).

## Zaključak
Ovaj projekat pruža osnovne funkcionalnosti za analizu online prodaje, rad sa proizvodima i korpom kupaca. Može se dodatno proširiti uvođenjem baza podataka, REST API-ja ili korisničkog interfejsa.

