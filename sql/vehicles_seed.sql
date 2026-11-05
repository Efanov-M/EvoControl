-- EvoControl / SQLite / 40 автомобилей
-- Тестовые вымышленные данные. Запускайте после применения миграций.
PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;


INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'А500КР77', 'Toyota', 'Camry', 'Белый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'А500КР77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'В501МС77', 'Kia', 'Rio', 'Чёрный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'В501МС77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Е502НТ77', 'Hyundai', 'Solaris', 'Серебристый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Е502НТ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'К503ОУ77', 'Volkswagen', 'Polo', 'Синий'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'К503ОУ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'М504РХ77', 'Skoda', 'Octavia', 'Красный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'М504РХ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Н505СА77', 'Renault', 'Duster', 'Серый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Н505СА77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'О506ТВ77', 'Lada', 'Vesta', 'Зелёный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'О506ТВ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Р507УЕ77', 'Nissan', 'Qashqai', 'Белый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Р507УЕ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'С508ХК77', 'Mazda', 'CX-5', 'Чёрный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'С508ХК77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Т509АМ77', 'Honda', 'Civic', 'Серебристый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Т509АМ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'У510ВН77', 'Ford', 'Focus', 'Синий'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'У510ВН77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Х511ЕО77', 'BMW', '320i', 'Красный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Х511ЕО77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'А512КР77', 'Mercedes-Benz', 'C180', 'Серый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'А512КР77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'В513МС77', 'Audi', 'A4', 'Зелёный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'В513МС77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Е514НТ77', 'Lexus', 'RX350', 'Белый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Е514НТ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'К515ОУ77', 'Subaru', 'Forester', 'Чёрный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'К515ОУ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'М516РХ77', 'Mitsubishi', 'Outlander', 'Серебристый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'М516РХ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Н517СА77', 'Geely', 'Coolray', 'Синий'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Н517СА77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'О518ТВ77', 'Haval', 'Jolion', 'Красный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'О518ТВ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Р519УЕ77', 'Chery', 'Tiggo 7', 'Серый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Р519УЕ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'С520ХК77', 'Volvo', 'XC60', 'Зелёный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'С520ХК77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Т521АМ77', 'Peugeot', '408', 'Белый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Т521АМ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'У522ВН77', 'Citroen', 'C4', 'Чёрный'
