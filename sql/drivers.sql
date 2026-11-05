-- EvoControl / SQLite / 15 водителей; требуется предварительный импорт эвакуаторов
-- Тестовые вымышленные данные. Запускайте после применения миграций.
PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;


INSERT INTO drivers_drivers (first_name, last_name, license_driver, country, tow_truck_id)
SELECT 'Иван', 'Иванов', '7700123000', 'Russia',
       (SELECT id FROM fleet_towtruck WHERE license_plate = 'А600МС77')
WHERE EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'А600МС77')
  AND NOT EXISTS (SELECT 1 FROM drivers_drivers WHERE license_driver = '7700123000');

INSERT INTO drivers_drivers (first_name, last_name, license_driver, country, tow_truck_id)
SELECT 'Пётр', 'Петров', '7700123001', 'Russia',
       (SELECT id FROM fleet_towtruck WHERE license_plate = 'В601НТ77')
WHERE EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'В601НТ77')
  AND NOT EXISTS (SELECT 1 FROM drivers_drivers WHERE license_driver = '7700123001');

INSERT INTO drivers_drivers (first_name, last_name, license_driver, country, tow_truck_id)
SELECT 'Алексей', 'Сидоров', '7700123002', 'Russia',
       (SELECT id FROM fleet_towtruck WHERE license_plate = 'Е602ОУ77')
WHERE EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'Е602ОУ77')
  AND NOT EXISTS (SELECT 1 FROM drivers_drivers WHERE license_driver = '7700123002');

INSERT INTO drivers_drivers (first_name, last_name, license_driver, country, tow_truck_id)
SELECT 'Дмитрий', 'Кузнецов', '7700123003', 'Russia',
       (SELECT id FROM fleet_towtruck WHERE license_plate = 'К603РХ77')
WHERE EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'К603РХ77')
  AND NOT EXISTS (SELECT 1 FROM drivers_drivers WHERE license_driver = '7700123003');

INSERT INTO drivers_drivers (first_name, last_name, license_driver, country, tow_truck_id)
SELECT 'Сергей', 'Смирнов', '7700123004', 'Russia',
       (SELECT id FROM fleet_towtruck WHERE license_plate = 'М604СА77')
WHERE EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'М604СА77')
  AND NOT EXISTS (SELECT 1 FROM drivers_drivers WHERE license_driver = '7700123004');

INSERT INTO drivers_drivers (first_name, last_name, license_driver, country, tow_truck_id)
SELECT 'Андрей', 'Попов', '7700123005', 'Russia',
       (SELECT id FROM fleet_towtruck WHERE license_plate = 'А600МС77')
WHERE EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'А600МС77')
  AND NOT EXISTS (SELECT 1 FROM drivers_drivers WHERE license_driver = '7700123005');

INSERT INTO drivers_drivers (first_name, last_name, license_driver, country, tow_truck_id)
SELECT 'Николай', 'Васильев', '7700123006', 'Russia',
       (SELECT id FROM fleet_towtruck WHERE license_plate = 'В601НТ77')
WHERE EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'В601НТ77')
  AND NOT EXISTS (SELECT 1 FROM drivers_drivers WHERE license_driver = '7700123006');

INSERT INTO drivers_drivers (first_name, last_name, license_driver, country, tow_truck_id)
SELECT 'Максим', 'Соколов', '7700123007', 'Russia',
       (SELECT id FROM fleet_towtruck WHERE license_plate = 'Е602ОУ77')
WHERE EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'Е602ОУ77')
  AND NOT EXISTS (SELECT 1 FROM drivers_drivers WHERE license_driver = '7700123007');

INSERT INTO drivers_drivers (first_name, last_name, license_driver, country, tow_truck_id)
SELECT 'Артём', 'Михайлов', '7700123008', 'Russia',
       (SELECT id FROM fleet_towtruck WHERE license_plate = 'К603РХ77')
WHERE EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'К603РХ77')
  AND NOT EXISTS (SELECT 1 FROM drivers_drivers WHERE license_driver = '7700123008');

INSERT INTO drivers_drivers (first_name, last_name, license_driver, country, tow_truck_id)
SELECT 'Егор', 'Новиков', '7700123009', 'Russia',
       (SELECT id FROM fleet_towtruck WHERE license_plate = 'М604СА77')
WHERE EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'М604СА77')
  AND NOT EXISTS (SELECT 1 FROM drivers_drivers WHERE license_driver = '7700123009');

INSERT INTO drivers_drivers (first_name, last_name, license_driver, country, tow_truck_id)
SELECT 'Кирилл', 'Фёдоров', '7700123010', 'Russia',
       (SELECT id FROM fleet_towtruck WHERE license_plate = 'А600МС77')
WHERE EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'А600МС77')
  AND NOT EXISTS (SELECT 1 FROM drivers_drivers WHERE license_driver = '7700123010');

INSERT INTO drivers_drivers (first_name, last_name, license_driver, country, tow_truck_id)
SELECT 'Олег', 'Морозов', '7700123011', 'Russia',
       (SELECT id FROM fleet_towtruck WHERE license_plate = 'В601НТ77')
WHERE EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'В601НТ77')
  AND NOT EXISTS (SELECT 1 FROM drivers_drivers WHERE license_driver = '7700123011');

INSERT INTO drivers_drivers (first_name, last_name, license_driver, country, tow_truck_id)
SELECT 'Павел', 'Волков', '7700123012', 'Russia',
       (SELECT id FROM fleet_towtruck WHERE license_plate = 'Е602ОУ77')
WHERE EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'Е602ОУ77')
  AND NOT EXISTS (SELECT 1 FROM drivers_drivers WHERE license_driver = '7700123012');

INSERT INTO drivers_drivers (first_name, last_name, license_driver, country, tow_truck_id)
SELECT 'Роман', 'Алексеев', '7700123013', 'Russia',
       (SELECT id FROM fleet_towtruck WHERE license_plate = 'К603РХ77')
WHERE EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'К603РХ77')
  AND NOT EXISTS (SELECT 1 FROM drivers_drivers WHERE license_driver = '7700123013');

INSERT INTO drivers_drivers (first_name, last_name, license_driver, country, tow_truck_id)
SELECT 'Виктор', 'Лебедев', '7700123014', 'Russia',
       (SELECT id FROM fleet_towtruck WHERE license_plate = 'М604СА77')
WHERE EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'М604СА77')
  AND NOT EXISTS (SELECT 1 FROM drivers_drivers WHERE license_driver = '7700123014');

COMMIT;
