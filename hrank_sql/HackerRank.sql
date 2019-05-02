

/* 7 */
/* Query distinct cities ending by vowels */

SELECT DISTINCT city
FROM station
WHERE city LIKE '%a' OR city LIKE '%e' OR city LIKE '%i' OR city LIKE '%o' OR city LIKE '%u'
ORDER BY 1;



/* 8 */
/* Query distinct cities with starting and ending by vowels */

SELECT DISTINCT city
FROM station
WHERE (city LIKE 'a%' OR city LIKE 'e%' OR city LIKE 'i%' OR city LIKE 'o%' OR city LIKE 'u%')
      AND
      (city LIKE '%a' OR city LIKE '%e' OR city LIKE '%i' OR city LIKE '%o' OR city LIKE '%u')
ORDER BY 1;

/* AN EASIER VERSION!!!! */

SELECT DISTINCT city
FROM station
WHERE city RLIKE '^[aeiou]' AND city RLIKE '[aeiou]$'

/* 9 */
/* Query distinct cities that do not start with vowels */

SELECT DISTINCT city
FROM station
WHERE city NOT RLIKE '^[aeiou]'
ORDER BY 1;

/* 10 */
/* Query distinct cities that do not end with vowels */

SELECT DISTINCT city
FROM station
WHERE city NOT RLIKE '[aeiou]$'
ORDER BY 1;

/* 11 */
/* Query distinct cities that do not start with vowels OR do not end with vowels */

SELECT DISTINCT city
FROM station
WHERE city NOT RLIKE '^[aeiou]' OR city NOT RLIKE '[aeiou]$'
ORDER BY 1;

/* 12 */
/* Query distinct cities that do not start AND do not end with vowels */
SELECT DISTINCT city
FROM station
WHERE city NOT RLIKE '^[aeiou]' AND city NOT RLIKE '[aeiou]$'
ORDER BY 1;

/* 13 */
/* Query students that scored higher than 75, order by the last 3 letter of students' name */

SELECT name
FROM students
WHERE marks > 75
ORDER BY RIGHT(name, 3), id ASC;
