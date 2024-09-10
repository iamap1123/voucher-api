# Voucher API
## Intro
  以 APIFlask 實作優惠券管理功能，SQLAlchemy 做為 ORM 框架，搭配 Marshmallow schema 驗證資料輸入及輸出格式，以 Docker 方式執行。

## How to use
  本專案包含 API App 及 MySQL DB，以 docker compose 方式運行，API 預設本機 port 為 `5001`，DB 預設為 `3307`：

  - 在專案根目錄下執行 `docker compose build`
  - 執行 docker container `docker compose up`
  - 首頁： http://127.0.0.1:5001/
  - Swagger UI： http://127.0.0.1:5001/docs#/

## Functions
  - 新增優惠券
  - 更新優惠券
  - 查詢所有優惠券
  - 以條件查詢優惠券
    - 優惠券名稱為模糊查詢，其餘欄位為精確查詢
  - 以 ID 查詢優惠券

## Data Validation
  - 新增必填欄位優惠券名稱、折扣金額、折扣百分比、優惠起始日/截止日、狀態
  - 優惠券名稱長度 (至少 1 個字，上限為 50 字)
  - 折扣金額需大於 0
  - 折扣百分比 (最小為 0.01，最大為 1)
  - 優惠起始日需小於截止日
  - 狀態只可為 "unused", "used", "expired" 三者其一

## File Structure

```
voucher-api
    ├── app/
    │    ├── .flaskenv
    │    ├── Dockerfile
    │    ├── app.py
    │    ├── config/
    │    │    ├── base_response.py
    │    │    └── db.py
    │    ├── models/
    │    │    └── voucher.py
    │    └── schemas/
    │         ├── voucher_schema.py
    │         └── date_validator.py
    ├── db/
    │    └── init.sql
    ├── docker-compose.yml
    ├── .gitignore
    └── README.md
```
## Table Schema
  ### Vouchsers

  |  Column   | Datatype  | Description | Remark |
  |  ----  | ----  | ----  | ---- | 
  | id  | BIGINT | ID | PK, AUTO_INCREMENT|
  | name | VARCHAR(50) | 優惠券名稱 | |
  | discount_amount | INTEGER | 折扣金額 | |
  | discount_percentage | INTEGER | 折扣百分比 | |
  | effective_date_from | DATE | 有效起始日 | |
  | effective_date_end | DATE | 有效截止日 | |
  | status | ENUM | 優惠券狀態 | 'unused', 'used', 'expired' |
  | valid | BOOLEAN | 是否可用 | 預設為 True |
  | created_at | DATETIME | 建立日期 | 預設建立時間 |
  | updated_at | DATETIME | 異動日期 | 預設更新時間 |
