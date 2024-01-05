import React from 'react';
import { Card, CardBody } from "@nextui-org/react";

const Description = () => {
    return (
        <div className="flex items-end">
                <Card className="rounded-md bg-zinc-800" style={{userSelect: "none", position: "absolute", transform: "translate(200%, 120%)"}}>
                    <CardBody className="flex flex-col gap-2 sm:gap-3 w-80">
                        <h1 className='text-2xl font-bold'>Welcome to our CS203 Project!</h1>
                        <h3 className='text-md'>Mark attendances; anywhere, anytime. 🙂</h3>
                    </CardBody>
                </Card>
        </div>
    );
};

export default Description;
