import React from "react";
import { QUIZZES } from "../../quizzes/quizzes";
import { useHistory } from "react-router-dom";

const HomePage = () => {
    const history = useHistory();

    return (
        <div>
            <div>
                <h2>Misquiz</h2>
            </div>
            <div>
                <ul>
                    {QUIZZES.map(quiz => (
                        <li
                            key={quiz.quiz}
                            className="list-disc"
                            onClick={() => {
                                const uri = "/" + encodeURI(quiz.quiz);
                                console.log(uri);
                                history.push(uri);
                            }}
                        >
                            {quiz.quiz}
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default HomePage;
