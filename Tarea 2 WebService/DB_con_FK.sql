select*from users
select*from todos
select*from albums


CREATE TABLE users (
    	user_id integer primary key,
    	name VARCHAR (255),
    	username VARCHAR (255),
	email VARCHAR (255),
	address VARCHAR (255),
	geo_lat VARCHAR (255),
	geo_lng VARCHAR (255),
	phone VARCHAR (255),
	website VARCHAR (255),
	company VARCHAR (255)
);

CREATE TABLE albums (
	userId integer,
	FOREIGN KEY (userId) REFERENCES users (user_id),
    	id integer primary key,
	title varchar(200)	
);

select*from albums
------------

CREATE TABLE todos (
    todos_id integer primary key,
	id_user integer,
	FOREIGN KEY (id_user) REFERENCES users (user_id),
	title varchar(200),
	completed varchar(100)	
);

select*from todos

CREATE TABLE photos (
    	photos_id integer primary key,
	id_albums integer,
	FOREIGN KEY (id_albums) REFERENCES albums (id),
	title varchar(500),
	url varchar(500),
	thumbnail_url varchar(500)
);


CREATE TABLE posts (
    	posts_id integer primary key,
	user_id integer,
	FOREIGN KEY (user_id) REFERENCES users (user_id),
	title varchar(500),
	body varchar(500)	
);


CREATE TABLE comments (
    	comments_id integer primary key,
	posts_id integer,
	FOREIGN KEY (posts_id) REFERENCES posts (posts_id),
	name varchar(500),
	email varchar(500),
	body varchar(500)
);

select*from users
select*from todos
select*from albums
select*from comments
select*from posts
select*from photos
