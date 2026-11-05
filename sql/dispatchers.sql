-- EvoControl / SQLite / 10 диспетчеров; требуется предварительный импорт стоянок
-- Тестовые вымышленные данные. Запускайте после применения миграций.
PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;


INSERT INTO dispatchers_dispatchers (first_name, last_name, employee_number, place_work_id, user_id)
SELECT 'Анна', 'Орлова', 'EVO-D001',
       (SELECT id FROM parking_parkinglot WHERE name = 'Тестовая стоянка Северная' ORDER BY id LIMIT 1), NULL
WHERE EXISTS (SELECT 1 FROM parking_parkinglot WHERE name = 'Тестовая стоянка Северная')
  AND NOT EXISTS (SELECT 1 FROM dispatchers_dispatchers WHERE employee_number = 'EVO-D001');

INSERT INTO dispatchers_dispatchers (first_name, last_name, employee_number, place_work_id, user_id)
SELECT 'Мария', 'Кузнецова', 'EVO-D002',
       (SELECT id FROM parking_parkinglot WHERE name = 'Тестовая стоянка Южная' ORDER BY id LIMIT 1), NULL
WHERE EXISTS (SELECT 1 FROM parking_parkinglot WHERE name = 'Тестовая стоянка Южная')
  AND NOT EXISTS (SELECT 1 FROM dispatchers_dispatchers WHERE employee_number = 'EVO-D002');

INSERT INTO dispatchers_dispatchers (first_name, last_name, employee_number, place_work_id, user_id)
SELECT 'Елена', 'Соколова', 'EVO-D003',
       (SELECT id FROM parking_parkinglot WHERE name = 'Тестовая стоянка Восточная' ORDER BY id LIMIT 1), NULL
WHERE EXISTS (SELECT 1 FROM parking_parkinglot WHERE name = 'Тестовая стоянка Восточная')
  AND NOT EXISTS (SELECT 1 FROM dispatchers_dispatchers WHERE employee_number = 'EVO-D003');

INSERT INTO dispatchers_dispatchers (first_name, last_name, employee_number, place_work_id, user_id)
SELECT 'Ольга', 'Волкова', 'EVO-D004',
       (SELECT id FROM parking_parkinglot WHERE name = 'Тестовая стоянка Западная' ORDER BY id LIMIT 1), NULL
WHERE EXISTS (SELECT 1 FROM parking_parkinglot WHERE name = 'Тестовая стоянка Западная')
  AND NOT EXISTS (SELECT 1 FROM dispatchers_dispatchers WHERE employee_number = 'EVO-D004');

INSERT INTO dispatchers_dispatchers (first_name, last_name, employee_number, place_work_id, user_id)
SELECT 'Наталья', 'Морозова', 'EVO-D005',
       (SELECT id FROM parking_parkinglot WHERE name = 'Тестовая стоянка Северная' ORDER BY id LIMIT 1), NULL
WHERE EXISTS (SELECT 1 FROM parking_parkinglot WHERE name = 'Тестовая стоянка Северная')
  AND NOT EXISTS (SELECT 1 FROM dispatchers_dispatchers WHERE employee_number = 'EVO-D005');

INSERT INTO dispatchers_dispatchers (first_name, last_name, employee_number, place_work_id, user_id)
SELECT 'Ирина', 'Фёдорова', 'EVO-D006',
       (SELECT id FROM parking_parkinglot WHERE name = 'Тестовая стоянка Южная' ORDER BY id LIMIT 1), NULL
WHERE EXISTS (SELECT 1 FROM parking_parkinglot WHERE name = 'Тестовая стоянка Южная')
  AND NOT EXISTS (SELECT 1 FROM dispatchers_dispatchers WHERE employee_number = 'EVO-D006');

INSERT INTO dispatchers_dispatchers (first_name, last_name, employee_number, place_work_id, user_id)
SELECT 'Светлана', 'Попова', 'EVO-D007',
       (SELECT id FROM parking_parkinglot WHERE name = 'Тестовая стоянка Восточная' ORDER BY id LIMIT 1), NULL
WHERE EXISTS (SELECT 1 FROM parking_parkinglot WHERE name = 'Тестовая стоянка Восточная')
  AND NOT EXISTS (SELECT 1 FROM dispatchers_dispatchers WHERE employee_number = 'EVO-D007');

INSERT INTO dispatchers_dispatchers (first_name, last_name, employee_number, place_work_id, user_id)
SELECT 'Татьяна', 'Лебедева', 'EVO-D008',
       (SELECT id FROM parking_parkinglot WHERE name = 'Тестовая стоянка Западная' ORDER BY id LIMIT 1), NULL
WHERE EXISTS (SELECT 1 FROM parking_parkinglot WHERE name = 'Тестовая стоянка Западная')
  AND NOT EXISTS (SELECT 1 FROM dispatchers_dispatchers WHERE employee_number = 'EVO-D008');

INSERT INTO dispatchers_dispatchers (first_name, last_name, employee_number, place_work_id, user_id)
SELECT 'Дарья', 'Смирнова', 'EVO-D009',
       (SELECT id FROM parking_parkinglot WHERE name = 'Тестовая стоянка Северная' ORDER BY id LIMIT 1), NULL
WHERE EXISTS (SELECT 1 FROM parking_parkinglot WHERE name = 'Тестовая стоянка Северная')
  AND NOT EXISTS (SELECT 1 FROM dispatchers_dispatchers WHERE employee_number = 'EVO-D009');

INSERT INTO dispatchers_dispatchers (first_name, last_name, employee_number, place_work_id, user_id)
SELECT 'Юлия', 'Алексеева', 'EVO-D010',
       (SELECT id FROM parking_parkinglot WHERE name = 'Тестовая стоянка Южная' ORDER BY id LIMIT 1), NULL
WHERE EXISTS (SELECT 1 FROM parking_parkinglot WHERE name = 'Тестовая стоянка Южная')
  AND NOT EXISTS (SELECT 1 FROM dispatchers_dispatchers WHERE employee_number = 'EVO-D010');

COMMIT;
