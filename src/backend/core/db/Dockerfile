# syntax=docker/dockerfile:1
FROM postgres:latest

# Copy database structure declaration and seeding script
# The database will be created with the right tables
# and prepopulated with data
COPY src/backend/core/db/seed.sql /docker-entrypoint-initdb.d/