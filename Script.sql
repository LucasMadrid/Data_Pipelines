create database stream_db;


create table stream_transactions(
	id serial primary key,
	transaction_id varchar(250),
	user_id varchar(250),
	amount float
	
);
