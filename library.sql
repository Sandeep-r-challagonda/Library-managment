-- 


--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `BookID` varchar(255) DEFAULT NULL,
  `BookTitle` varchar(255) DEFAULT NULL,
  `author_name` varchar(255) DEFAULT NULL,
  `publication_company` varchar(255) DEFAULT NULL,
  `Rented_date` varchar(255) DEFAULT NULL,
  `Rented_user` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES ('462416216','The Alchemist','Paulo Coelho','HarperCollins',' ','available'),('462060631','The Song of Achilles','Madeline Miller','HarperCollins',' ','available'),('470550625','Borderline Personality Disorder For Dummies','Charles H. Elliott','Wiley',' ','available'),('476788494','Romeo and Juliet','William Shakespeare','Simon & Schuster',' ','available'),('220820387','Python Programming from Beginner to Paid Professional','A. J. Wright','A. J. Wright',' ','available'),('743237352','The Torrents of Spring','Ernest Hemingway','Scribner',' ','available'),('626819023','A Checklist for Murder','Anthony Flacco','Open Road Integrated Media',' ','available'),('536662177','Stillhouse Lake','Rachel Caine','Brilliance Audio','30-03-2022','745'),('562838223','Eight Perfect Murders','Peter Swanson','HarperAudio','01-04-2022','Narendra'),('jsnfanf','Updated_title','Updated author','updated publisher','',''),('462416216','The Alchemist','Paulo Coelho','HarperCollins',' ','available'),('462060631','The Song of Achilles','Madeline Miller','HarperCollins',' ','available'),('470550625','Borderline Personality Disorder For Dummies','Charles H. Elliott','Wiley',' ','available'),('476788494','Romeo and Juliet','William Shakespeare','Simon & Schuster',' ','available'),('220820387','Python Programming from Beginner to Paid Professional','A. J. Wright','A. J. Wright',' ','available'),('743237352','The Torrents of Spring','Ernest Hemingway','Scribner',' ','available'),('626819023','A Checklist for Murder','Anthony Flacco','Open Road Integrated Media',' ','available'),('536662177','Stillhouse Lake','Rachel Caine','Brilliance Audio',' ','available'),('562838223','Eight Perfect Murders','Peter Swanson','HarperAudio','01-04-2022','Narendra'),('9781490000000.0','Living Forward: A Proven Plan to Stop Drifting and Get the Life You Want','Michael Hyatt','Baker Publishing Group',' ','available'),('9781630000000.0','Activate Your Brain: How Understanding Your Brain Can Improve Your Work - and Your Life','Scott G. Halford','Greenleaf Book Group',' ','available');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `librarians`
--

DROP TABLE IF EXISTS `librarians`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `librarians` (
  `Librarian_Id` int DEFAULT NULL,
  `Librarian_name` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `librarians`
--

LOCK TABLES `librarians` WRITE;
/*!40000 ALTER TABLE `librarians` DISABLE KEYS */;
INSERT INTO `librarians` VALUES (78546201,'test_name','9898752'),(78546201,'test_name','9898752'),(78546201,'test_name','9898752'),(123420,'test_librarian','123456789'),(85647123,'traveller','+5641200987');
/*!40000 ALTER TABLE `librarians` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members` (
  `MemberID` varchar(255) DEFAULT NULL,
  `Member_name` varchar(255) DEFAULT NULL,
  `contact_number` varchar(255) DEFAULT NULL,
  `penalty_fees` varchar(255) DEFAULT NULL,
  `Notifications` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES ('JOTARO_575994','JOTARO','100',' ','0'),('TEST_USER_799477','TEST_USER','420','0',' '),('test_user_956518','test_user','100','0',' '),('aldo_838577','aldo','800','0',' '),('gz_803173','gz','hz','0',' '),('hz_990032','hz','hz','0',' '),('bfhj_222702','bfhj','500','0',' '),('zu_446801','zu','tr','0',' '),('tets_name_150272','tets_name','741','0',' '),('OP_853712','Updated name','+1 7856423004778','0',' '),('OP_742149','OP','OP','0',' '),('OP_850219','OP','OP','0',' '),('OP2_331871','OP2','OP2','0',' '),('narendra _484331','narendra ','789','0',' '),('sandeep_683388','sandeep','987','0',' '),('test_name_982032','test_name','test_number','0',' '),('alpha_339149','alpha','8585201','0',' '),('Joseph_669225','Joseph','89898989','0',' '),('joseph_168702','joseph','8989','0',' '),('jojo_359382','jojo','897','0',' '),('tzr_404331','tzr','789','0',' '),('rsggh_147158','rsggh','thth','0',' '),('202_913720','202','320','0',' '),('745_952993','745','updated_number','0',' '),('Narendra_966128','Narendra','520321420','0',' '),('magician_215451','magician','+1 250 3687 58210','0',' '),('alpha_romeo_104310','alpha_romeo','564789231','0',' '),('test_name_814965','test_name','9898752','0',' ');
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-02  4:27:41
