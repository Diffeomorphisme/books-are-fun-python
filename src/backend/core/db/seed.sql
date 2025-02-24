CREATE TABLE "book" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"title" varchar NOT NULL
);

INSERT INTO book (title) VALUES
 ('Dune Part III'),
 ('Strange Weather in Tokyo'),
 ('Circe'),
 ('Achilles'),
 ('Changer l''eau des fleurs')
;