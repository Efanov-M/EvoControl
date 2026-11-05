-- EvoControl / SQLite / 5 эвакуаторов
-- Тестовые вымышленные данные. Запускайте после применения миграций.
PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;


INSERT INTO fleet_towtruck (license_plate, brand, model, truck_type, vin, is_active)
SELECT 'А600МС77', 'ГАЗ', 'ГАЗон NEXT', 'platform', NULL, 1
WHERE NOT EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'А600МС77');

INSERT INTO fleet_towtruck (license_plate, brand, model, truck_type, vin, is_active)
SELECT 'В601НТ77', 'Hyundai', 'HD78', 'platform', NULL, 1
WHERE NOT EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'В601НТ77');

INSERT INTO fleet_towtruck (license_plate, brand, model, truck_type, vin, is_active)
SELECT 'Е602ОУ77', 'Isuzu', 'NPR75', 'manipulator', NULL, 1
WHERE NOT EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'Е602ОУ77');

INSERT INTO fleet_towtruck (license_plate, brand, model, truck_type, vin, is_active)
SELECT 'К603РХ77', 'КАМАЗ', 'Компас 9', 'platform', NULL, 1
WHERE NOT EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'К603РХ77');

INSERT INTO fleet_towtruck (license_plate, brand, model, truck_type, vin, is_active)
SELECT 'М604СА77', 'JAC', 'N90', 'manipulator', NULL, 1
WHERE NOT EXISTS (SELECT 1 FROM fleet_towtruck WHERE license_plate = 'М604СА77');

COMMIT;
