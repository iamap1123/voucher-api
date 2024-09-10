CREATE DATABASE assignment CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
use assignment;

CREATE TABLE vouchers (
  id BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  discount_amount INTEGER NOT NULL,
  discount_percentage DECIMAL(3,2) NOT NULL,
  effective_date_from DATE NOT NULL,
  effective_date_end DATE NOT NULL,
  status ENUM('unused', 'used', 'expired'),
  valid BOOLEAN DEFAULT 1,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO vouchers
  (name, discount_amount, discount_percentage, effective_date_from, effective_date_end,
   status, valid)
VALUES
  ('99 大折扣', 150, 0.15, '2024-09-09', '2024-09-30', 'unused', 1),
  ('滿兩千送兩百', 200, 0.1, '2024-09-09', '2024-09-30', 'unused', 1);