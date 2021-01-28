# Pickle_Unpickle_scheduling
This repository is a demo for handling the scheduling the serialization and deserialization of an object to a pickle file<br/>


# How to reproduce the error:<br/>

In the terminal:<br/>
python database_update.py<br/>

In another terminal:<br/>
python rec_service.py<br/>

You should run into an EOF Error. This happens due to the command of dump and load the same pickle file at the same time.<br/>


# Potential Solution:<br/>
First terminal:<br/>
python database_update.py<br/>
Second terminal:<br/>
python rec_service_exception_handled.py<br/>

You should see the miss rate for 1000 tries<br/>


Solution useful for integration into any project:<br/>
First terminal:<br/>
python database_update.py<br/>
Second terminal:<br/>
python rec_service_exception_handled_integrate.py<br/>
