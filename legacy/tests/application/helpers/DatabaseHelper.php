<?php

class DatabaseHelper
{
    private static $super_connection;
    private static $connection;

    public static function getSuperuserConnection()
    {
        if (is_null(self::$super_connection)) {
            $config = Config::getConfig();
            $db_host = $config['dsn']['host'];
            $db_port = $config['dsn']['port'];

            self::$super_connection = pg_connect("host={$db_host} port={$db_port} user=postgres password=password");
        }

        return self::$super_connection;
    }

    public static function getConnection()
    {
        if (is_null(self::$connection)) {
            $config = Config::getConfig();
            $db_host = $config['dsn']['host'];
            $db_port = $config['dsn']['port'];
            $db_name = $config['dsn']['database'];
            $db_username = $config['dsn']['username'];
            $db_password = $config['dsn']['password'];

            self::$connection = pg_connect("host={$db_host} port={$db_port} dbname={$db_name} user={$db_username} password={$db_password}");
        }

        return self::$connection;
    }

    public static function createUser()
    {
        $config = Config::getConfig();
        $db_username = $config['dsn']['username'];
        $db_password = $config['dsn']['password'];

        $con = self::getSuperuserConnection();
        pg_query($con, "CREATE USER {$db_username} WITH PASSWORD '{$db_password}';");
    }

    public static function dropUser()
    {
        $config = Config::getConfig();
        $db_username = $config['dsn']['username'];
        $con = self::getSuperuserConnection();
        pg_query($con, "DROP USER IF EXISTS {$db_username};");
    }

    public static function databaseExists($name)
    {
        $con = self::getSuperuserConnection();
        $result = pg_query($con, "SELECT 1 FROM pg_database WHERE datname='{$name}';");
        if (!$result) {
            return false;
        }

        return pg_fetch_result($result, 0, 0) == 1;
    }

    public static function createTemplateDatabase()
    {
        $con = self::getSuperuserConnection();

        pg_query($con, "CREATE DATABASE libretime_template WITH ENCODING 'UTF8' TEMPLATE template0;");

        $files = ['schema.sql', 'defaultdata.sql'];
        foreach ($files as $file) {
            $sql = file_get_contents(ROOT_PATH . '/build/sql/' . $file);
            pg_query($con, $sql);
        }

        $seed_tables = ['cc_files', 'cc_music_dirs', 'cc_pref', 'cc_show', 'cc_show_days', 'cc_show_instance'];

        foreach ($seed_tables as $seed_table) {
            $path = __DIR__ . '/' . $seed_table . '.csv';
            pg_query($con, "COPY {$seed_table} FROM '{$path}' WITH (FORMAT csv)");
        }

        pg_query($con, "UPDATE pg_database SET datistemplate='true' WHERE datname='libretime_template';");
    }

    public static function dropTemplateDatabase()
    {
        $con = self::getSuperuserConnection();
        pg_query($con, "UPDATE pg_database SET datistemplate='false' WHERE datname='libretime_template';");
        self::dropDatabase('libretime_template');
    }

    public static function createDatabase()
    {
        $config = Config::getConfig();
        $db_name = $config['dsn']['database'];
        $db_username = $config['dsn']['username'];

        $con = self::getSuperuserConnection();
        pg_query($con, "CREATE DATABASE {$db_name} WITH ENCODING 'UTF8' TEMPLATE libretime_template OWNER {$db_username};");
    }

    public static function dropDatabase()
    {
        $config = Config::getConfig();
        $db_name = $config['dsn']['database'];
        $con = self::getSuperuserConnection();
        pg_query($con, "DROP DATABASE IF EXISTS {$db_name};");
    }
}
