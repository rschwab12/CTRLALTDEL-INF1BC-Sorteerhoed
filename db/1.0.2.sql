INSERT INTO `db_versions` (`id`, `version`, `creator`, `created`) VALUES (NULL, '1.0.2', 'Rico Schwab', CURRENT_TIMESTAMP);
ALTER TABLE sorteerhoed.answers DROP FOREIGN KEY answers_specalisations;
ALTER TABLE `answers` DROP `specialisationId`;
ALTER TABLE `answers` DROP `weight`;
ALTER TABLE `answers` ADD `iat` INT(11) NOT NULL DEFAULT '0' AFTER `text`, ADD `fict` INT(11) NOT NULL DEFAULT '0' AFTER `iat`, ADD `bdam` INT(11) NOT NULL DEFAULT '0' AFTER `fict`, ADD `se` INT(11) NOT NULL DEFAULT '0' AFTER `bdam`; 