-- SQLite
SELECT [id_area], [area], [descripcion]
FROM puesto AS a
INNER JOIN area AS b ON a.id_area = b.id;


-- Delete rows from table 'publicacion'
-- Select rows from a Tablpublicacion' in schema 'SchemaName'
SELECT * FROM publicacion;