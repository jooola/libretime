LibreTime uses PostgreSQL as the Database engine. In order to track changes to the schema, there are directories under [/airtime_mvc/application/controllers](https://github.com/LibreTime/libretime/tree/master/airtime_mvc/application/controllers) that dictate how to upgrade and downgrade the database schema.

Since LibreTime currently uses the PropelORM v1 there are a number of additional steps that you need to perform every time you want to change the schema. This is located in the [/airtime_mvc/build/schema.xml](https://github.com/LibreTime/libretime/tree/master/airtime_mvc/build/schema.xml) file.

Once you have made a change to this file you need to run propel-gen from inside of the `airtime_mvc/build` directory running `../../vendor/propel/propel1/generator/bin/propel-gen ` or `../../vendor/bin/propel-gen` should recreate the propel php classes to contain your schema change.

Once you have done this, you need to update Django's model of the database in [/api/libretimeapi/models/](https://github.com/LibreTime/libretime/tree/master/api/libretimeapi/models/).

You will also need to tell the application itself how to upgrade users by adding a new model to [airtime-mvc/application/upgrade/Upgrades.php](https://github.com/LibreTime/libretime/blob/master/airtime_mvc/application/upgrade/Upgrades.php) and translating the schema change directly into postgresql code in a new directory under `airtime_mvc/application/controllers/upgrade_sql/airtime_3.0.0-alpha.VERSIONNUMBER/upgrade.sql` and how to undo the change under `airtime_mvc/application/controllers/downgrade_sql/airtime_3.0.0-alpha.VERSIONNUMBER/downgrade.sql`

See these lines of code

```
class AirtimeUpgrader300alpha7 extends AirtimeUpgrader
{
    protected function getSupportedSchemaVersions() {
        return array(
            '3.0.0-alpha.6'
        );
    }

    public function getNewVersion() {
        return '3.0.0-alpha.7';
    }
}
```

for an example of the Upgrades.php function that is needed for each database change. You will need to build off of a previous schema version so you might need to refactor a PR a couple of times if other database schemas are merged after you wrote your PR.

Historically, the project has used the same versioning for the database schema as the LibreTime releases. This made it difficult to keep the database up to date if users were running LibreTime from the tip of git. Thus it was [decided](https://github.com/LibreTime/libretime/pull/776#issuecomment-478557387) to add be more granular with the schema version. Any change that requires modifying the database should include directories under `/airtime_mvc/application/controllers/upgrade_sql/` and `/airtime_mvc/application/controllers/downgrade_sql/` that increment by a decimal based upon the latest release.

For example if we are working on alpha.8 release and a couple of database commits have already been merged and you see
public function getNewVersion() {
return '3.0.0-alpha.8.2';
} in Upgrades.php then you should create the files for your next database change `airtime_3.0.0-alpha.8.3/upgrade.sql` and airtime_3.0.0-alpha.3.0.0-alpha.8.3/downgrade.sql and add

```
 /**
  * Class AirtimeUpgrader300alpha8-3
  *
  * GH-#PRNUMBER - link to github PR pull and brief description of database change for future reference  */

class AirtimeUpgrader300alpha8-3 extends AirtimeUpgrader
{
    protected function getSupportedSchemaVersions() {
        return array(
            '3.0.0-alpha.8.2'
        );
    }
```

and update this to version to

```
    public function getNewVersion() {
        return '3.0.0-alpha.8.3';
    }
```

in addition to changing the schema.xml file and regenerating the propel boiler plate classes as described above. If someone notices a conflict when trying to merge a PR that was targeting the same version then you might need to increment.

This allows us to keep our database schema changes underneath the same version number while allowing incremental changes to people who are running off of the latest git master.
