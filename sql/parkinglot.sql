-- EvoControl / SQLite / 4 стоянки
-- Тестовые вымышленные данные. Запускайте после применения миграций.
PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;


INSERT INTO parking_parkinglot (name, address, is_active)
SELECT 'Тестовая стоянка Северная', 'г. Москва, ул. Дубнинская, д. 10', 1
WHERE NOT EXISTS (SELECT 1 FROM parking_parkinglot WHERE name = 'Тестовая стоянка Северная');

INSERT INTO parking_parkinglot (name, address, is_active)
SELECT 'Тестовая стоянка Южная', 'г. Москва, ул. Подольских Курсантов, д. 14', 1
WHERE NOT EXISTS (SELECT 1 FROM parking_parkinglot WHERE name = 'Тестовая стоянка Южная');

INSERT INTO parking_parkinglot (name, address, is_active)
SELECT 'Тестовая стоянка Восточная', 'г. Москва, ул. Перовская, д. 65', 1
WHERE NOT EXISTS (SELECT 1 FROM parking_parkinglot WHERE name = 'Тестовая стоянка Восточная');

INSERT INTO parking_parkinglot (name, address, is_active)
SELECT 'Тестовая стоянка Западная', 'г. Москва, ул. Рябиновая, д. 28', 1
WHERE NOT EXISTS (SELECT 1 FROM parking_parkinglot WHERE name = 'Тестовая стоянка Западная');

COMMIT;
