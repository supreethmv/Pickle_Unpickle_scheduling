# Pickle_Unpickle_scheduling
This repository is a demo for handling the scheduling the serialization and deserialization of an object to a pickle file


How to reproduce the error:

In the terminal:
python database_update.py

In another terminal:
python rec_service.py

You should run into an EOF Error. This happens due to the command of dump and load the same pickle file at the same time.


Potential Solution:
First terminal:
python database_update.py
Second terminal:
python rec_service_exception_handled.py

You should see the miss rate for 1000 tries


Solution useful for integration into any project:
First terminal:
python database_update.py
Second terminal:
python rec_service_exception_handled_integrate.py
