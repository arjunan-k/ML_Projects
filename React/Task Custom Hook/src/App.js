import React, { useEffect, useState } from 'react';
import Tasks from './components/Tasks/Tasks';
import NewTask from './components/NewTask/NewTask';
import useHttp from './hooks/use-http';

const URL = "Firebase Url"

function App() {
  const [tasks, setTasks] = useState([]);

  // const transformTasks = tasksObj => {
  //   const loadedTasks = [];

  //   for (const taskKey in tasksObj) {
  //     loadedTasks.push({ id: taskKey, text: tasksObj[taskKey].text });
  //   }

  //   setTasks(loadedTasks);
  // }

  const httpData = useHttp()
  const {isLoading, error, sendRequest: fetchTasks} = httpData

  useEffect(() => {
    const transformTasks = tasksObj => {
      const loadedTasks = [];
  
      for (const taskKey in tasksObj) {
        loadedTasks.push({ id: taskKey, text: tasksObj[taskKey].text });
      }
  
      setTasks(loadedTasks);
    }

    fetchTasks({url: URL}, transformTasks);
  }, []);

  const taskAddHandler = (task) => {
    setTasks((prevTasks) => prevTasks.concat(task));
  };

  return (
    <React.Fragment>
      <NewTask onAddTask={taskAddHandler} />
      <Tasks
        items={tasks}
        loading={isLoading}
        error={error}
        onFetch={fetchTasks}
      />
    </React.Fragment>
  );
}

export default App;