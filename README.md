# flask-example
Flask example application

## Resolving dependencies

```shell
pip install flask-mysql
```

## How to initialize database
type `​mysql -u root -p` and type again

```sql
CREATE DATABASE blog;

USE blog;

CREATE TABLE IF NOT EXISTS `blog` (
`articleNumber` int(10) unsigned NOT NULL auto_increment COMMENT '글번호',
`title` mediumtext collate utf8_unicode_ci NOT NULL COMMENT '제목',
`content` varchar(1000) collate utf8_unicode_ci NOT NULL COMMENT '본문',
UNIQUE KEY `articleNumber` (`articleNumber`)
);

show tables;

insert into blog (title, content) values("title", "body");
``` 