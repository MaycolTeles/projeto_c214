USE `db`;

CREATE TABLE IF NOT EXISTS `comprovante_residencia` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `value` VARCHAR(255) NOT NULL,
    `date` DATE NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `cpf` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `value` VARCHAR(255) NOT NULL,
    `date` DATE NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `rg` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `value` VARCHAR(255) NOT NULL,
    `date` DATE NOT NULL,
    PRIMARY KEY (`id`)
);
