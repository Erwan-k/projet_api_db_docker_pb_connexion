 SET NAMES utf8 ;
DROP TABLE IF EXISTS `commentaires`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `commentaires` (
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  `visible` int(1) DEFAULT NULL,
  `date` int(10) DEFAULT NULL,
  `adresse_mail` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `commentaires` WRITE;

UNLOCK TABLES;
DROP TABLE IF EXISTS `Parent`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Parent` (
  `adresse_mail` varchar(255) DEFAULT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `mdp` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Parent` WRITE;

UNLOCK TABLES;
DROP TABLE IF EXISTS `Adresse_mail_non_verif`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Adresse_mail_non_verif` (
  `adresse_mail` varchar(255) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Adresse_mail_non_verif` WRITE;

UNLOCK TABLES;
DROP TABLE IF EXISTS `Token`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Token` (
  `adresse_mail` varchar(255) DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Token` WRITE;

UNLOCK TABLES;
DROP TABLE IF EXISTS `Code_modif_mdp`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Code_modif_mdp` (
  `adresse_mail` varchar(255) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Code_modif_mdp` WRITE;

UNLOCK TABLES;
DROP TABLE IF EXISTS `Messagerie`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Messagerie` (
  `adresse_mail` varchar(255) DEFAULT NULL,
  `expediteur` varchar(255) DEFAULT NULL,
  `destinataire` varchar(255) DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  `date` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Messagerie` WRITE;

UNLOCK TABLES;
DROP TABLE IF EXISTS `Eleve`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Eleve` (
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `class` varchar(255) DEFAULT NULL,
  `lycee` varchar(255) DEFAULT NULL,
  `adresse_mail_parent` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Eleve` WRITE;

UNLOCK TABLES;
DROP TABLE IF EXISTS `Disponibilites`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Disponibilites` (
  `id` int(6) DEFAULT NULL,
  `nom_eleve` varchar(255) DEFAULT NULL,
  `prenom_eleve` varchar(255) DEFAULT NULL,
  `heure_debut` varchar(255) DEFAULT NULL,
  `heure_fin` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Disponibilites` WRITE;

UNLOCK TABLES;
