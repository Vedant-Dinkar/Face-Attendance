import React, { useState, useEffect, useRef } from "react";
import {
  Table,
  TableHeader,
  TableBody,
  TableColumn,
  TableRow,
  TableCell,
  Button,
} from "@nextui-org/react";
import { Card, CardBody } from "@nextui-org/react";
import axios from "axios";

function StagingArea({ data }) {
  return (
    <Card className="rounded-md bg-zinc-800">
      <CardBody className="flex flex-col gap-2 sm:gap-3">
        {data.map((item, index) => (
          <div key={index} className="flex flex-row gap-2 items-center">
            <p className="w-48 text-sm">{item.name}</p>
          </div>
        ))}
      </CardBody>
    </Card>
  );
}

const FileUploader = ({ setPayload, roll }) => {
  const fileUploader = useRef();

  const handleFileChange = (e) => {
    setPayload((prev) => ({
      ...prev,
      [roll]: { file: e.target.files[0], name: e.target.files[0].name },
    }));
  };

  return (
    <>
      <input
        accept=".png, .jpg, .jpeg"
        hidden
        type="file"
        ref={fileUploader}
        onChange={handleFileChange}
        required
      />
      <Button
        onPress={() => fileUploader.current.click()}
        className="bg-zinc-700 text-zinc-100 font-medium w-24"
        radius="sm"
        size="md"
      >
        Add files
      </Button>
    </>
  );
};


export default function Config() {
  const [studentData, setStudentData] = useState([]);
  const [selectedFiles, setSelectedFiles] = useState({});
  const fileUploaders = useRef({});

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/courses", {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((response) => {
        console.log(response.data.stulist);
        setStudentData(response.data.stulist);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }, []);

  const fileSubmit = () => {
    const formData = new FormData();

    Object.entries(selectedFiles).forEach(([roll, fileObj, names]) => {
      formData.append("files", fileObj.file, fileObj.name);
      formData.append("rollNumbers", roll);
      formData.append("names", names);
    });

    axios.post("http://127.0.0.1:8000/cours", formData)
    .then(response => {
    })
    .catch(error => {
      console.error("Error:", error);
    });

    console.log(formData);
  };

  return (
    <div className="w-screen h-screen flex justify-center p-2">
      <div className="lg:w-3/5 w-screen">
        <Table aria-label="Example static collection table">
          <TableHeader>
            <TableColumn>Roll Number</TableColumn>
            <TableColumn>Name</TableColumn>
            <TableColumn>Upload</TableColumn>
          </TableHeader>
          <TableBody>
            {studentData.map((item) => (
              <TableRow key={item[0]}>
                <TableCell>{item[1]}</TableCell>
                <TableCell>{item[0]}</TableCell>
                <TableCell>
                  {selectedFiles[item[1]] && (
                    <StagingArea
                      data={[{ name: selectedFiles[item[1]].name }]}
                    />
                  )}
                  <span className="w-full flex flex-row justify-end mt-4">
                    {!selectedFiles[item[1]] && (
                      <FileUploader
                        setPayload={setSelectedFiles}
                        roll={item[1]}
                      />
                    )}
                  </span>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
        <Button
          onPress={fileSubmit}
          className="bg-zinc-700 text-zinc-100 font-medium w-24"
          radius="sm"
          size="md"
          
        >
          Submit All
        </Button>
      </div>
    </div>
  );
}
