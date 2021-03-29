
<?php

class DailyCodingUser 
{
    private $database = null;
    public function __construct() {
        $this->database = new db('host','user','pass','db');
    }
    public function getUsers() {
        return $this->database->getAll('users');
    }
}

$user = new DailyCodingUser();
$user->getUsers();

The class User has an implicit dependency on a specific database. 
All dependencies should always be explicit rather than implicit.
This defeats the dependency inversion principle.

If we wanted to change database credentials, we need to edit the DailyCodingUser class. 
Dependency Injection makes testing easier.

Possible solution:

<?php
class DailyCodingUser 
{
    private $database = null;
    public function __construct(Database $database) {
        $this->database = $database;
    }
    public function getUsers() {
        return $this->database->getAll('users');
    }
}

$database = new Database('host', 'user', 'pass', 'dbname');
$user = new DailyCodingUser($database);
$user->getUsers();


