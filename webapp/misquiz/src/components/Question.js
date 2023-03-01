import React from "react";
import Answer from "./quiz/Answer";

const Question = (question, answers, help, isFinished) => {
    return (
        <div>
            <div>
                <h1>{question}</h1>
            </div>
            <div>
                {
                    <ul>
                        {answers.map(answer => (
                            <div>
                                <Answer
                                    isCorrect={answer.isCorrect}
                                    text={answer.answer}
                                />
                            </div>
                        ))}
                    </ul>
                }
            </div>
            {isFinished && <div>{help}</div>}
        </div>
    );
};

export default Question;
