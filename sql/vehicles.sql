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
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'У522ВН77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Х523ЕО77', 'Opel', 'Astra', 'Серебристый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Х523ЕО77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'А524КР77', 'Suzuki', 'Vitara', 'Синий'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'А524КР77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'В525МС77', 'Changan', 'CS55', 'Красный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'В525МС77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Е526НТ77', 'Exeed', 'TXL', 'Серый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Е526НТ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'К527ОУ77', 'Omoda', 'C5', 'Зелёный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'К527ОУ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'М528РХ77', 'Jetour', 'Dashing', 'Белый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'М528РХ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Н529СА77', 'GAC', 'GS8', 'Чёрный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Н529СА77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'О530ТВ77', 'Toyota', 'RAV4', 'Серебристый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'О530ТВ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Р531УЕ77', 'Kia', 'Sportage', 'Синий'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Р531УЕ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'С532ХК77', 'Hyundai', 'Tucson', 'Красный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'С532ХК77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Т533АМ77', 'Volkswagen', 'Tiguan', 'Серый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Т533АМ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'У534ВН77', 'Skoda', 'Kodiaq', 'Зелёный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'У534ВН77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Х535ЕО77', 'Renault', 'Logan', 'Белый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Х535ЕО77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'А536КР77', 'Lada', 'Granta', 'Чёрный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'А536КР77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'В537МС77', 'Nissan', 'X-Trail', 'Серебристый'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'В537МС77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'Е538НТ77', 'Mazda', '6', 'Синий'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'Е538НТ77');

INSERT INTO vehicles_vehicle (license_plate, brand, model, color)
SELECT 'К539ОУ77', 'Honda', 'CR-V', 'Красный'
WHERE NOT EXISTS (SELECT 1 FROM vehicles_vehicle WHERE license_plate = 'К539ОУ77');

COMMIT;
