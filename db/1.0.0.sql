SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
  `text` varchar(255) NOT NULL,
  `specialisationId` int(11) NOT NULL,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `db_versions`
--

CREATE TABLE `db_versions` (
  `id` int(11) NOT NULL,
  `version` varchar(11) NOT NULL,
  `creator` varchar(255) NOT NULL,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Gegevens worden geëxporteerd voor tabel `db_versions`
--

INSERT INTO `db_versions` (`id`, `version`, `creator`, `created`) VALUES
(2, '1.0.0', 'Rico Schwab', '2020-10-12 14:08:55');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `questions`
--

CREATE TABLE `questions` (
  `questionId` int(11) NOT NULL,
  `text` varchar(1024) NOT NULL,
  `type` int(11) NOT NULL,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `specialisations`
--

CREATE TABLE `specialisations` (
  `specialisationId` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `answers`
--
ALTER TABLE `answers`
  ADD PRIMARY KEY (`answerId`),
  ADD KEY `questionId` (`questionId`),
  ADD KEY `specialisationId` (`specialisationId`);

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
-- Indexen voor tabel `specialisations`
--
ALTER TABLE `specialisations`
  ADD PRIMARY KEY (`specialisationId`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `answers`
--
ALTER TABLE `answers`
  MODIFY `answerId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT voor een tabel `db_versions`
--
ALTER TABLE `db_versions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT voor een tabel `questions`
--
ALTER TABLE `questions`
  MODIFY `questionId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT voor een tabel `specialisations`
--
ALTER TABLE `specialisations`
  MODIFY `specialisationId` int(11) NOT NULL AUTO_INCREMENT;

--
-- Beperkingen voor geëxporteerde tabellen
--

--
-- Beperkingen voor tabel `answers`
--
ALTER TABLE `answers`
  ADD CONSTRAINT `answers_questions` FOREIGN KEY (`questionId`) REFERENCES `questions` (`questionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `answers_specalisations` FOREIGN KEY (`specialisationId`) REFERENCES `specialisations` (`specialisationId`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
