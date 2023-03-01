import React from "react";

const Answer = (isCorrect, text, isAnswered, isSelected) => {
    const classCorrect =
        isAnswered && isCorrect && isSelected ? "bg-green-200" : "bg-red-200";

    return (
        <div className={isAnswered ? classCorrect : ""}>
            <p>{text}</p>
        </div>
    );
};

export default Answer;
