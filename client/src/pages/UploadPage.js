import { Card, CardBody } from "@nextui-org/react";
import { Button, ButtonGroup } from "@nextui-org/react";
import { ChangeEvent, useRef, useState } from "react";
import axios from "axios";

// const all_present = ["220001004", "220001002", "220001003", "220001004"];
// const all_files = ["file_name1.png", "file_name2.png"];

function StagingArea({ data, name }) {
  return (
    <Card className="rounded-md bg-zinc-700" style={{userSelect: "none", overflowY: "scroll", height:"100px", boxShadow: "inset 0 0 10px rgba(0, 0, 0, 0.3"}}>
      <CardBody className="flex flex-col gap-2 sm:gap-3">
        {data.length === 0 ? (
          <p className="text-sm text-zinc-400">*Add files to display</p>
        ) : (
          data.map((item, index) => (
            <div key={index} className="flex flex-row gap-2 items-center">
              <p className="w-48 text-sm">{item.name}</p>
            </div>
          ))
        )}
      </CardBody>
    </Card>
  );
}

function exportCSV() {
  fetch("http://127.0.0.1:8000/exportcsv")
    .then((response) => response.blob())
    .then((blob) => {
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      const date = new Date();
      link.href = url;
      link.setAttribute('download', 'final-attendance'+String(date)+'.csv');
      document.body.appendChild(link);
      link.click();
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function AllPresent({ data, name }) {
  return (
    <Card className="rounded-md bg-zinc-700" style={{overflowY: "scroll", height: "125px", boxShadow: "inset 0 0 10px rgba(0, 0, 0, 0.3"}}>
      <CardBody className="flex flex-col gap-2 sm:gap-3">
        {data.map((item, index) => (
          <div key={index} className="flex flex-row gap-2 items-center">
            <p className="w-48 text-sm">{item}</p>
          </div>
        ))}
      </CardBody>
    </Card>
  );
}

export default function HomePage() {
  const fileUploader = useRef();
  const [selectedFile, setSelectedFile] = useState([]);
  const [allPresent, setAllPresent] = useState([]);

  console.log(selectedFile[0])
  function fileSubmit() {
    const formData = new FormData();

    selectedFile.forEach((file) => formData.append("files", file));
    // console.log(formData);
    setAllPresent([]);
    axios
      .post("http://127.0.0.1:8000/uploadfiles", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((response) => {
        console.log(response.data.present)
        setAllPresent(response.data.present);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
  console.log(selectedFile);
  return (
    <div className="bg-zinc-900" style={{height: '100vh', overflowY: "hidden", backgroundImage: 'url("https://www.bypeople.com/wp-content/uploads/2014/05/dark-svg-background-image.jpg")', backgroundSize: "repeat", "background-color": "#000000", "background-image": `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Cg fill-rule='evenodd'%3E%3Cg fill='%239C92AC' fill-opacity='0.4'%3E%3Cpath opacity='.5' d='M96 95h4v1h-4v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h4v1h-4v9h4v1h-4v9h4v1h-4v9h4v1h-4v9h4v1h-4v9h4v1h-4v9h4v1h-4v9h4v1h-4v9zm-1 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-9-10h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm9-10v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-9-10h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm9-10v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-9-10h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm9-10v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-9-10h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9z'/%3E%3Cpath d='M6 5V0H5v5H0v1h5v94h1V6h94V5H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")`}}>
      <div className="flex w-full justify-center p-4">
        <div className="w-96 flex flex-col gap-4 bg-zinc-800" style={{marginTop: '0%', borderRadius: '24px', padding: '30px', height: '80%'}}>
          <p className="text-2xl font-bold bg-gradient-to-br from-red-500 to-blue-500 text-transparent bg-clip-text text-stroke text-stroke-white" style={{userSelect: "none"}}>Take Attendance</p>
          <div className="flex flex-col gap-2">
            <p className=" font-medium" style={{userSelect: "none"}}>Uploaded Image(s):</p>
            <StagingArea data={selectedFile} name="file" />
            <span className="w-full flex flex-row justify-end mt-4 gap-4"  style={{userSelect: "none"}}>
              <Button
                onPress={() => fileUploader.current.click()}
                className="bg-zinc-700 text-zinc-100 font-medium w-24 bg-gradient-to-br from-red-500 to-blue-500 hover:bg-gradient-to-br hover:from-red-600 hover:to-blue-600 transition-all duration-500 ease-in-out transform hover:scale-105"
                radius="sm"
                size="md"
              >
                Add files
              </Button>
              <Button
                onPress={fileSubmit}
                className="bg-zinc-700 text-zinc-100 font-medium w-24 bg-gradient-to-br from-red-500 to-blue-500 hover:bg-gradient-to-br hover:from-red-600 hover:to-blue-600 transition-all duration-500 ease-in-out transform hover:scale-105"
                radius="sm"
                size="md"
              >
                Submit
              </Button>
            </span>

            <input
              accept=".png, .jpg, .jpeg"
              //   this doesn't really prevent the user from uploading anyways
              hidden
              type="file"
              ref={fileUploader}
              onChange={(e) =>
                setSelectedFile([...selectedFile, e.target.files[0]])
              }
            />
          </div>

          <div className="flex flex-col gap-2">
            <p className=" font-medium"  style={{userSelect: "none"}}>Student(s) Present:</p>
            <AllPresent data={allPresent} name="present" />
            <span className="w-full flex flex-row justify-end mt-4 gap-4">
            <Button
              className="bg-zinc-700 text-zinc-100 font-medium w-24 bg-gradient-to-br from-red-500 to-blue-500 hover:bg-gradient-to-br hover:from-red-600 hover:to-blue-600 transition-all duration-500 ease-in-out transform hover:scale-105"
              radius="sm"
              size="md"
              onPress={exportCSV}
            >
                Export CSV
              </Button>
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}
