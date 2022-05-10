<?php

/**
 * @internal
 *
 * @coversNothing
 */
class DatabaseTestCase extends PHPUnit_Framework_TestCase
{
    // public static function setUpBeforeClass()
    // {
    //     echo 'Creating user!' . PHP_EOL;
    //     DatabaseHelper::createUser();
    //     echo 'Creating template database!' . PHP_EOL;
    //     DatabaseHelper::createTemplateDatabase();
    // }

    public function setUp()
    {
        echo 'Creating database!' . PHP_EOL;
        DatabaseHelper::createDatabase();
    }

    public function tearDown()
    {
        echo 'Dropping database!' . PHP_EOL;
        DatabaseHelper::dropDatabase();
    }

    // public static function tearDownAfterClass()
    // {
    //     echo 'Dropping template database!' . PHP_EOL;
    //     DatabaseHelper::dropTemplateDatabase();
    //     echo 'Dropping user!' . PHP_EOL;
    //     DatabaseHelper::dropUser();
    // }
}
