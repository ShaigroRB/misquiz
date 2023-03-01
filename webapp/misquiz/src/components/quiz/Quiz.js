import React from "react";
import Question from "../Question";

const Quiz = (quiz) => {
    console.log(typeof(questions))
    return (
        <div>
            <div>
                <h1>{quiz.quiz.quiz}</h1>
            </div>
            <div>
                {
                    <ul>
                        {/* {questions.map(question => (
                            <Question
                                question={question.question}
                                answers={question.answers}
                                help={question.help}
                            />
                        ))} */}
                        <li>ks</li>
                    </ul>
                }
            </div>
        </div>
    );
};

export default Quiz;