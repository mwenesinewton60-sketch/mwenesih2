<?php

function findGrade($score) {
    if ($score >=70){
        return "A";
    } elseif ($score >=60){
        return "B";
    }elseif ($score >=50){
        return "C";
    }elseif ($score >=40){
        return "D";
    }elseif ($score <=39){
        return "E";
    }else{
        return "Be serious!";
    }
}
 echo "Enter your the students actual name:";
 $name = trim(fgets(STDIN));

 echo "Enter your the students score:";
 $score = trim(fgets(STDIN));

 $grade = findGrade($score);
 
 echo "\nStudent Name: $name\n";
 echo "Student Score: $score\n";
 echo "Student Grade: $grade\n";

 ?>