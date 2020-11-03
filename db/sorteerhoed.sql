-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Gegenereerd op: 03 nov 2020 om 00:27
-- Serverversie: 10.3.25-MariaDB-0ubuntu0.20.04.1
-- PHP-versie: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sorteerhoed`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `answers`
--

CREATE TABLE `answers` (
  `answerId` int(11) NOT NULL,
  `questionId` int(11) NOT NULL,
  `text` varchar(500) NOT NULL,
  `iat` int(11) NOT NULL DEFAULT 0,
  `fict` int(11) NOT NULL DEFAULT 0,
  `bdam` int(11) NOT NULL DEFAULT 0,
  `se` int(11) NOT NULL DEFAULT 0,
  `position` int(11) NOT NULL DEFAULT 0,
  `created` datetime NOT NULL DEFAULT current_timestamp(),
  `updated` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Gegevens worden geëxporteerd voor tabel `answers`
--

INSERT INTO `answers` (`answerId`, `questionId`, `text`, `iat`, `fict`, `bdam`, `se`, `position`, `created`, `updated`) VALUES
(1, 1, 'Ja', 2, 0, 0, 0, 1, '2020-10-27 12:50:48', '2020-10-27 12:50:48'),
(2, 1, 'Nee', 0, 0, 0, 0, 2, '2020-10-27 12:50:57', '2020-10-27 12:50:57'),
(3, 1, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 12:51:07', '2020-10-27 12:51:07'),
(4, 2, 'Ja', 0, 0, 2, 0, 1, '2020-10-27 12:51:40', '2020-10-27 12:51:40'),
(5, 2, 'Nee', 0, 0, 0, 0, 2, '2020-10-27 12:51:57', '2020-10-27 12:51:57'),
(6, 2, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 12:52:14', '2020-10-27 12:52:14'),
(7, 3, 'Ja', 0, 2, 0, 1, 1, '2020-10-27 12:53:52', '2020-10-27 12:53:52'),
(8, 3, 'Nee', 0, 0, 0, 0, 2, '2020-10-27 12:54:01', '2020-10-27 12:54:01'),
(9, 3, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 12:54:24', '2020-10-27 12:54:24'),
(10, 4, 'Ja', 2, 0, 0, 0, 1, '2020-10-27 12:54:43', '2020-10-27 12:54:43'),
(11, 4, 'Nee', 0, 0, 0, 0, 2, '2020-10-27 12:54:50', '2020-10-27 12:54:50'),
(12, 13, 'Eens', 0, 2, 0, 0, 1, '2020-10-27 12:56:01', '2020-10-27 12:56:01'),
(13, 13, 'Oneens', 0, 0, 0, 0, 2, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(14, 13, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(15, 14, 'Eens', 0, 2, 0, 0, 1, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(16, 14, 'Oneens', 0, 0, 0, 0, 2, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(17, 14, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(18, 7, 'Eens', 2, 2, 0, 0, 1, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(19, 7, 'Oneens', 0, 0, 0, 0, 2, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(20, 7, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(21, 8, 'Eens', 2, 2, 2, 0, 1, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(22, 8, 'Oneens', 0, 0, 0, 0, 2, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(23, 8, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(29, 9, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(30, 9, 'Oneens', 0, 0, 0, 0, 2, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(33, 10, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(34, 10, 'Oneens', 0, 0, 0, 0, 2, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(35, 10, 'Eens', 0, 0, 0, 2, 1, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(38, 11, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(39, 11, 'Oneens', 0, 0, 0, 0, 2, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(40, 11, 'Eens', 2, 0, 0, 0, 1, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(41, 12, 'Eens', 2, 0, 0, 0, 1, '2020-10-27 13:04:38', '2020-10-27 13:04:38'),
(42, 12, 'Oneens', 0, 0, 0, 0, 2, '2020-10-27 13:04:38', '2020-10-27 13:04:38'),
(43, 12, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 13:04:38', '2020-10-27 13:04:38'),
(46, 5, 'Ja', 0, 0, 0, 2, 1, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(47, 5, 'Nee', 0, 0, 0, 0, 2, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(48, 5, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(49, 6, 'Ja', 0, 0, 0, 2, 1, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(50, 6, 'Nee', 0, 0, 0, 0, 2, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(51, 6, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(52, 18, 'Je bent onderzoekend en een doorzetter. Jij bent niet bang voor een beetje data, maar ziet juist plezier in het verwerken van data.', 0, 0, 2, 0, 1, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(53, 18, 'Je bent analytisch, doelgericht en vasthoudend. Je bent innovatief, nieuwsgierig naar de nieuwe technologieën en de mogelijkheden die ze bieden. Verder kan je goed omgaan met mensen en je weet ze naar waarde in te schatten.', 0, 2, 0, 0, 2, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(54, 18, 'Je bent creatief, kritisch en bent niet bang voor technologie. Jij houdt ervan om jezelf uit te dagen en werkt graag met de nieuwste technologieën. Je kan goed samenwerken, hebt en positieve mentaliteit en een nieuwsgierige houding naar de nieuwste technologieën.', 2, 0, 0, 0, 3, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(55, 18, 'Je hebt een sterk analytisch vermogen. Je ontwerp en programmeert graag en bent niet bang voor een uitdaging.', 0, 0, 0, 2, 4, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(56, 16, 'Eens', 0, 1, 2, 0, 1, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(57, 16, 'Oneens', 0, 0, 0, 0, 2, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(58, 16, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(59, 17, 'Eens', 2, 0, 0, 0, 1, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(60, 17, 'Oneens', 0, 0, 0, 0, 2, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(61, 15, 'Eens', 0, 2, 0, 2, 1, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(62, 15, 'Oneens', 0, 0, 0, 0, 2, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(63, 19, 'Ontwikkel een Virtual Reality app via het web met een nieuwe technologie en schrijf op basis van jouw bevindingen een adviesrapport voor anderen die er ook mee aan de slag willen.', 2, 0, 0, 0, 1, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(64, 19, 'Maak op basis van klikgedrag in een webshop een voorspellende analyse van producten die de klant waarschijnlijk ook wil aanschaffen. Deze producten kun je dan attenderen tijdens het browsen en bij het afronden van de bestelling.', 0, 0, 2, 0, 2, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(65, 19, 'Doe onderzoek naar een laptop die door de politie in beslag is genomen. Je zoekt digitale sporen op zodanige wijze dat dit geaccepteerd bewijsmateriaal oplevert ten behoeve van de rechtelijke vervolging. Je besteedt dus veel tijd aan de verslaglegging van het onderzoek.', 0, 2, 0, 0, 3, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(66, 19, 'Met een groot team van developers ontwikkel je een systeem voor de onlinebibliotheek. Je programmeert veel, overlegt met je collega’s en houdt contact met de opdrachtgever.', 0, 0, 0, 2, 4, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(67, 20, 'Software Engineer of Technical Designer', 0, 0, 0, 2, 1, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(68, 20, 'Digitaal rechercheur of Ethical Hacker', 0, 2, 0, 0, 2, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(69, 20, 'Business Intelligence consultant of Data Scientist', 0, 0, 2, 0, 3, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(70, 20, 'Interaction Designer of Desktoppublisher', 2, 0, 0, 0, 4, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(71, 9, 'Eens', 0, 0, 2, 0, 1, '2020-10-27 12:56:07', '2020-10-27 12:56:07'),
(72, 4, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 12:54:50', '2020-10-27 12:54:50'),
(73, 17, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 13:08:38', '2020-10-27 13:08:38'),
(74, 15, 'Neutraal', 0, 0, 0, 0, 3, '2020-10-27 13:08:38', '2020-10-27 13:08:38');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `db_versions`
--

CREATE TABLE `db_versions` (
  `id` int(11) NOT NULL,
  `version` varchar(11) NOT NULL,
  `creator` varchar(255) NOT NULL,
  `created` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Gegevens worden geëxporteerd voor tabel `db_versions`
--

INSERT INTO `db_versions` (`id`, `version`, `creator`, `created`) VALUES
(1, '1.0.0', 'Rico Schwab', '2020-10-12 14:08:55'),
(2, '1.0.1', 'Rico Schwab', '2020-10-27 12:48:07'),
(3, '1.0.2', 'Rico Schwab', '2020-10-27 12:49:39');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `questions`
--

CREATE TABLE `questions` (
  `questionId` int(11) NOT NULL,
  `text` varchar(1024) NOT NULL,
  `type` int(11) NOT NULL,
  `created` datetime NOT NULL DEFAULT current_timestamp(),
  `updated` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Gegevens worden geëxporteerd voor tabel `questions`
--

INSERT INTO `questions` (`questionId`, `text`, `type`, `created`, `updated`) VALUES
(1, 'Vind je het leuk vind je het om na te denken over hoe technologie beter kan?', 1, '2020-10-16 11:13:39', '2020-10-16 11:13:39'),
(2, 'Vind je het leuk om veel met data te werken?', 1, '2020-10-27 12:37:06', '2020-10-27 12:37:06'),
(3, 'Vind je het leuk om slimme wegen te vinden die leiden naar een oplossing? ', 1, '2020-10-27 12:37:15', '2020-10-27 12:37:15'),
(4, 'Ben je creatief ingesteld?', 1, '2020-10-27 12:37:23', '2020-10-27 12:37:23'),
(5, 'Vind je het interessant om te onderzoeken wat er nodig is voor het ontwikkelen van een systeem en daarbij rekening te houden met al bestaande systemen? ', 1, '2020-10-27 12:38:55', '2020-10-27 12:38:55'),
(6, 'Zou je graag willen werken aan het realiseren van AI-gerelateerde software? ', 1, '2020-10-27 12:39:02', '2020-10-27 12:39:02'),
(7, 'Ik ben nieuwsgierig naar de nieuwste technologieën en bereid hierover te leren.', 1, '2020-10-27 12:38:13', '2020-10-27 12:38:13'),
(8, 'Onderzoek doen vind ik leuk', 1, '2020-10-27 12:38:23', '2020-10-27 12:38:23'),
(9, 'Ik vind het leuk om grote hoeveelheden data te analyseren en verwerken.', 1, '2020-10-27 12:38:28', '2020-10-27 12:38:28'),
(10, 'Ik vind het leuk om grote infrastructuren te bouwen, te testen, en te realiseren. ', 1, '2020-10-27 12:38:34', '2020-10-27 12:38:34'),
(11, 'Ik vind het leuk om naar de behoefte van klanten slimme robots te bouwen om te helpen met taken die zei niet meer willen/kunnen doen. ', 1, '2020-10-27 12:38:43', '2020-10-27 12:38:43'),
(12, 'Ik vind het leuk om samen met eindgebruikers te discussiëren over de inrichting van een applicatie ', 1, '2020-10-27 12:38:50', '2020-10-27 12:38:50'),
(13, 'Ik vind het interessant om de juridische aspecten van informatica te leren.', 1, '2020-10-27 12:37:47', '2020-10-27 12:37:47'),
(14, 'Ik kan zorgvuldig werken en vindt het leuk om veel verslag te leggen.', 1, '2020-10-27 12:37:58', '2020-10-27 12:37:58'),
(15, 'Ik wil kennis hebben over bepaalde software zodat ik bedrijven kan adviseren in deze keuzes ', 1, '2020-10-27 12:39:35', '2020-10-27 12:39:35'),
(16, 'Bedrijfsprocessen interesseren mij en ik wil hier meer kennis en inzicht over hebben. ', 1, '2020-10-27 12:39:18', '2020-10-27 12:39:18'),
(17, 'Ik wil mijn kennis en creativiteit inzetten om de beste gebruikersinteractie te realiseren ', 1, '2020-10-27 12:39:24', '2020-10-27 12:39:24'),
(18, 'Waar herken jij je het meeste in? ', 1, '2020-10-27 12:39:11', '2020-10-27 12:39:11'),
(19, 'Welk onderstaand project zou jij het liefst uitvoeren? ', 1, '2020-10-27 12:39:41', '2020-10-27 12:39:41'),
(20, 'Als je één van onderstaande beroepen later zou mogen uitvoeren, welke zou je dan kiezen? ', 1, '2020-10-27 12:39:49', '2020-10-27 12:39:49');

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `answers`
--
ALTER TABLE `answers`
  ADD PRIMARY KEY (`answerId`),
  ADD KEY `questionId` (`questionId`);

--
-- Indexen voor tabel `db_versions`
--
ALTER TABLE `db_versions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `version` (`version`);

--
-- Indexen voor tabel `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`questionId`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `answers`
--
ALTER TABLE `answers`
  MODIFY `answerId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;

--
-- AUTO_INCREMENT voor een tabel `db_versions`
--
ALTER TABLE `db_versions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT voor een tabel `questions`
--
ALTER TABLE `questions`
  MODIFY `questionId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Beperkingen voor geëxporteerde tabellen
--

--
-- Beperkingen voor tabel `answers`
--
ALTER TABLE `answers`
  ADD CONSTRAINT `answers_questions` FOREIGN KEY (`questionId`) REFERENCES `questions` (`questionId`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
