import { Routes, Route } from "react-router-dom";
import UploadPage from "./pages/UploadPage";
import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import Courses from "./pages/Courses";
import Config from "./pages/Config";
import Register from "./pages/Register";

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<HomePage />}></Route>
        <Route path="/home" element={<HomePage />}></Route>
        <Route path="/courses" element={<Courses />}></Route>
        <Route path="/upload" element={<UploadPage />}></Route>
        <Route path="/login" element={<LoginPage />}></Route> 
        <Route path="/config" element={<Config />}></Route>  
        <Route path="/register" element={<Register />}></Route>       
      </Routes>
    </>
  );
}

export default App;

