<?php

/**
 * @internal
 *
 * @coversNothing
 */
class BlockDbTest extends DatabaseTestCase
{
    private $_connectionMock;

    public function setUp()
    {
        TestHelper::setupZendBootstrap();
        parent::setUp();
    }

    public function getConnection()
    {
        if ($this->_connectionMock == null) {
            $config = TestHelper::getDbZendConfig();

            $connection = Zend_Db::factory('pdo_pgsql', $config);

            $this->_connectionMock = $this->createZendDbConnection(
                $connection,
                'airtimeunittests'
            );
            Zend_Db_Table_Abstract::setDefaultAdapter($connection);
        }

        return $this->_connectionMock;
    }

    /**
     * Test if the single newest file is added to the Database.
     */
    public function testGetListofFilesMeetCriteriaSingleMatch()
    {
        TestHelper::loginUser();
        $CC_CONFIG = Config::getConfig();
        $testqry = CcFilesQuery::create();
        $testout = $testqry->find();
        $vd = $testout->getData();
        $ds = new Zend_Test_PHPUnit_Db_DataSet_QueryDataSet(
            $this->getConnection()
        );
        $testCriteria = BlockModelData::getCriteriaSingleNewestLabelNada();
        $bltest = new Application_Model_Block();
        $bltest->saveSmartBlockCriteria($testCriteria);
        $tracks = $bltest->getListOfFilesUnderLimit();
        // $tracks = $bltest->getLength();
        $this->assertNotEmpty($tracks);
        // need to load a example criteria into the database
    }

    /**
     * Test if the single newest file is added to the Database.
     */
    public function testMultiTrackandAlbumsGetLoaded()
    {
        TestHelper::loginUser();
        $CC_CONFIG = Config::getConfig();
        $testqry = CcFilesQuery::create();
        $testout = $testqry->find();
        $vd = $testout->getData();
        $ds = new Zend_Test_PHPUnit_Db_DataSet_QueryDataSet(
            $this->getConnection()
        );
        $testCriteria = BlockModelData::getCriteriaMultiTrackAndAlbum1Hour();
        $bltest = new Application_Model_Block();
        $bltest->saveSmartBlockCriteria($testCriteria);
        $tracks = $bltest->getListOfFilesUnderLimit();
        // $tracks = $bltest->getLength();
        $this->assertNotEmpty($tracks);
        // add assertion that the length is less than 1 hour...
        // need to load a example criteria into the database
    }
}
