const character = '@';
const rows = [];
const inverted = true;
const count = 10;

function padRow(rowNumber, rowCount) {
    return " ".repeat(rowCount - rowNumber) + character.repeat(2 * rowNumber - 1) + " ".repeat(rowCount - rowNumber)
}

for( let i = 1; i <= count; i++) {
    if(inverted) {
        rows.unshift(padRow(i, count))
    } else {
        rows.push(padRow(i, count))
    }
}

let result = " "

for(const row of rows) {
    result = result +  "\n" + row;
}

console.log(result.trim())

// Grade book

function getAverage(scores) {
    let sum = 0;
    for (let i = 0; i < scores.length; i++) {
      sum += scores[i];
    }
    return sum / scores.length;
  }
  
  function getGrade(score) {
    if (score == 100) {
      return "A++";
    } else if (score >= 90) {
      return "A";
    } else if (score >= 80) {
      return "B";
    } else if (score >= 70) {
      return "C";
    } else if (score >= 60) {
      return "D";
    } else {
      return "F";
    }
  }
  
  function studentMsg(totalScores, studentScore) {
    const average = getAverage(totalScores);
    const score = getGrade(studentScore);
    
    if (score != 'F') {
      return "Class average: " + average + ". Your grade: " + score + ". You passed the course.";
    } else {
      return "Class average: " + average + ". Your grade: " + score + ". You failed the course.";
    }
  }
  
  console.log(studentMsg([92, 88, 12, 77, 57, 100, 67, 38, 97, 89], 37)); // Class average: 71.7. Your grade: F. You failed the course.
  