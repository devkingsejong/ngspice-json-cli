# ngspice-json-cli
Print NGSPICE result as JSON

[![](https://img.shields.io/badge/Ngspice-27%2C34-orange)]()
[![](https://img.shields.io/badge/Python-3.8%2C3.9-blue)]()

ngspice-json-cli can

1. Simulate Ngspice circuit.(via ngspice program)
2. Get ngspice printed result as Json type

## How to install

1. Install ngspice

Click the right link to download Ngspice. [download ngspice](http://ngspice.sourceforge.net/download.html)

Currently, the version 27 and 34 have been confirmed to be support.

2. Install ngspice-json-cli from git 

```
> git clone https://github.com/devkingsejong/ngspice-json-cli.git
> cd ngspice-json-cli
> pip install -r ngspicejson/requirements.txt
```

3. Test run
```
> python3 ngspicejson/ngspice_json_cli.py run --command="" --file="ngspicejson/default_test_circuit.cir" --debug="True"
```

That command will be returned json array.

## Basic Usage

### Command

Command|Notes|
|---------|---|
|run|The simulation result is print in the data type mentioned below.(You can use --option value.)|
|version|Print version information.|

#### +a Version ouput.
```
{"ngspice": "34", "ngspice-json-cli": "0.0.1"}
```

### Options

Command|Notes|required|
|---------|---|-|
|--command STR|You can designate the command to be executed after loading the circuit in Ngspice.|Y|
|--file PATH|Please specify the path of the circuit code to be simulated in Ngspice.|Y|
|--tag STR|If you want to print the tag with the result, enter the tag value.(Ignore False value of the debug option.)|N|
|--debug BOOL|If you want to print the debug messages, set value to true.|N|
|--real BOOL|If you want to print the original Ngspice output, set value to true.|N|

### Data Types

#### NGSPICE_CLI_ERROR
Displays errors returned by the Ngspice program.(This data type is always assigned as the first value in the list

```json
{
   "type":"NGSPICE_CLI_ERROR",
   "contents":[
      "Error: no such vector 2"
   ],
   "real":""
}
```

#### INITIAL_TRANSIENT_SOLUTION
Parse Initialnal Trainsient Solution Value.

<details>
<summary>open/close button</summary>
<div markdown="1">

```json
{
      "type":"INITIAL_TRANSIENT_SOLUTION",
      "contents":[
         {
            "node":"int",
            "values":[
               {
                  "key":"Voltage",
                  "values":[
                     "0"
                  ]
               }
            ]
         },
         {
            "node":"in",
            "values":[
               {
                  "key":"Voltage",
                  "values":[
                     "0"
                  ]
               }
            ]
         },
         {
            "node":"out",
            "values":[
               {
                  "key":"Voltage",
                  "values":[
                     "0"
                  ]
               }
            ]
         },
         {
            "node":"v1#branch",
            "values":[
               {
                  "key":"Voltage",
                  "values":[
                     "0"
                  ]
               }
            ]
         }
      ],
      "real":""
   }
```

</div>
</details>



#### NODEMODEL
Parse Node Model's Value.(In general, this value printed when the 'show all ' command is executed.)

<details>
<summary>open/close button</summary>
<div markdown="1">

```json
 {
      "type":"NODEMODEL",
      "contents":[
         {
            "title":"Capacitor",
            "description":"Fixed capacitor",
            "contents":[
               {
                  "model":"c2",
                  "values":[
                     {
                        "key":"model",
                        "values":[
                           "C"
                        ]
                     },
                     {
                        "key":"capacitance",
                        "values":[
                           "1e-07"
                        ]
                     },
                     {
                        "key":"dtemp",
                        "values":[
                           "0"
                        ]
                     },
                     {
                        "key":"bv_max",
                        "values":[
                           "1e+99"
                        ]
                     },
                     {
                        "key":"i",
                        "values":[
                           "4.28591e-05"
                        ]
                     },
                     {
                        "key":"p",
                        "values":[
                           "4.06377e-06"
                        ]
                     }
                  ]
               },
               {
                  "model":"c1",
                  "values":[
                     {
                        "key":"model",
                        "values":[
                           "C"
                        ]
                     },
                     {
                        "key":"capacitance",
                        "values":[
                           "1e-06"
                        ]
                     },
                     {
                        "key":"dtemp",
                        "values":[
                           "0"
                        ]
                     },
                     {
                        "key":"bv_max",
                        "values":[
                           "1e+99"
                        ]
                     },
                     {
                        "key":"i",
                        "values":[
                           "0.000443373"
                        ]
                     },
                     {
                        "key":"p",
                        "values":[
                           "6.10419e-05"
                        ]
                     }
                  ]
               }
            ]
         },
         {
            "title":"Resistor",
            "description":"Simple linear resistor",
            "contents":[
               {
                  "model":"r2",
                  "values":[
                     {
                        "key":"model",
                        "values":[
                           "R"
                        ]
                     },
                     {
                        "key":"resistance",
                        "values":[
                           "1000"
                        ]
                     },
                     {
                        "key":"ac",
                        "values":[
                           "1000"
                        ]
                     },
                     {
                        "key":"dtemp",
                        "values":[
                           "0"
                        ]
                     },
                     {
                        "key":"bv_max",
                        "values":[
                           "1e+99"
                        ]
                     },
                     {
                        "key":"noisy",
                        "values":[
                           "1"
                        ]
                     },
                     {
                        "key":"i",
                        "values":[
                           "-4.28591e-05"
                        ]
                     },
                     {
                        "key":"p",
                        "values":[
                           "1.8369e-06"
                        ]
                     }
                  ]
               },
               {
                  "model":"r1",
                  "values":[
                     {
                        "key":"model",
                        "values":[
                           "R"
                        ]
                     },
                     {
                        "key":"resistance",
                        "values":[
                           "10000"
                        ]
                     },
                     {
                        "key":"ac",
                        "values":[
                           "10000"
                        ]
                     },
                     {
                        "key":"dtemp",
                        "values":[
                           "0"
                        ]
                     },
                     {
                        "key":"bv_max",
                        "values":[
                           "1e+99"
                        ]
                     },
                     {
                        "key":"noisy",
                        "values":[
                           "1"
                        ]
                     },
                     {
                        "key":"i",
                        "values":[
                           "-0.000486232"
                        ]
                     },
                     {
                        "key":"p",
                        "values":[
                           "0.00236422"
                        ]
                     }
                  ]
               }
            ]
         },
         {
            "title":"Vsource",
            "description":"Independent voltage source",
            "contents":[
               {
                  "model":"v1",
                  "values":[
                     {
                        "key":"dc",
                        "values":[
                           "0"
                        ]
                     },
                     {
                        "key":"acmag",
                        "values":[
                           "0"
                        ]
                     },
                     {
                        "key":"pulse",
                        "values":[
                           "0",
                           "5",
                           "1e-06",
                           "1e-06",
                           "1e-06",
                           "1",
                           "1"
                        ]
                     },
                     {
                        "key":"sin",
                        "values":[
                           "0",
                           "5",
                           "1e-06",
                           "1e-06",
                           "1e-06",
                           "1",
                           "1"
                        ]
                     },
                     {
                        "key":"exp",
                        "values":[
                           "0",
                           "5",
                           "1e-06",
                           "1e-06",
                           "1e-06",
                           "1",
                           "1"
                        ]
                     },
                     {
                        "key":"pwl",
                        "values":[
                           "0",
                           "5",
                           "1e-06",
                           "1e-06",
                           "1e-06",
                           "1",
                           "1"
                        ]
                     },
                     {
                        "key":"sffm",
                        "values":[
                           "0",
                           "5",
                           "1e-06",
                           "1e-06",
                           "1e-06",
                           "1",
                           "1"
                        ]
                     },
                     {
                        "key":"am",
                        "values":[
                           "0",
                           "5",
                           "1e-06",
                           "1e-06",
                           "1e-06",
                           "1",
                           "1"
                        ]
                     },
                     {
                        "key":"trnoise",
                        "values":[
                           "0",
                           "5",
                           "1e-06",
                           "1e-06",
                           "1e-06",
                           "1",
                           "1"
                        ]
                     },
                     {
                        "key":"trrandom",
                        "values":[
                           "0",
                           "5",
                           "1e-06",
                           "1e-06",
                           "1e-06",
                           "1",
                           "1"
                        ]
                     },
                     {
                        "key":"i",
                        "values":[
                           "-0.000486232"
                        ]
                     },
                     {
                        "key":"p",
                        "values":[
                           "-0.00243116"
                        ]
                     }
                  ]
               }
            ]
         }
      ],
      "real":""
   }
```

</div>
</details>

#### NGSPICE_VERSION
Parse Ngspice Verison.

```json
{
   "type":"NGSPICE_VERSION",
   "contents":[
      {
         "key":"version",
         "values":[
            "34"
         ]
      }
   ],
   "real": ""
}  
```

#### TABULARCONTENTS
Parse Tabular Contents(In general, this value printed when the 'print' command is executed.)

If there are multiple print statements in the circuit, result data will be separated printed like "print_#1".

<details>
<summary>open/close button</summary>
<div markdown="1">

```json
{
      "type":"TABULARCONTENTS",
      "contents":[
         {
            "key":"print_#1",
            "values":[
               {
                  "data_name":"time",
                  "values":[
                     "0.000000e+00",
                     "1.000000e-08",
                     "2.000000e-08",
                     "4.000000e-08",
                     "8.000000e-08",
                     "1.600000e-07",
                     "3.200000e-07",
                     "6.400000e-07",
                     "1.000000e-06",
                     "1.005125e-06",
                     "1.015374e-06",
                     "1.035874e-06",
                     "1.061343e-06",
                     "1.112281e-06",
                     "1.214156e-06",
                     "1.417908e-06",
                     "1.633075e-06",
                     "1.969139e-06",
                     "2.000000e-06",
                     "2.047146e-06",
                     "2.141437e-06",
                     "2.330020e-06",
                     "2.707185e-06",
                     "3.461515e-06",
                     "4.970176e-06",
                     "7.987498e-06",
                     "1.398750e-05",
                     "1.998750e-05",
                     "2.598750e-05",
                     "3.198750e-05",
                     "3.798750e-05",
                     "4.398750e-05",
                     "4.998750e-05",
                     "5.598750e-05",
                     "6.198750e-05",
                     "6.798750e-05",
                     "7.398750e-05",
                     "7.998750e-05",
                     "8.598750e-05",
                     "9.198750e-05",
                     "9.798750e-05",
                     "1.039875e-04",
                     "1.099875e-04",
                     "1.159875e-04",
                     "1.219875e-04",
                     "1.279875e-04",
                     "1.339875e-04",
                     "1.399875e-04",
                     "1.459875e-04",
                     "1.519875e-04",
                     "1.579875e-04",
                     "1.639875e-04",
                     "1.699875e-04",
                     "1.759875e-04",
                     "1.819875e-04",
                     "1.879875e-04",
                     "1.939875e-04",
                     "1.999875e-04",
                     "2.059875e-04",
                     "2.119875e-04",
                     "2.179875e-04",
                     "2.239875e-04",
                     "2.299875e-04",
                     "2.359875e-04",
                     "2.419875e-04",
                     "2.479875e-04",
                     "2.539875e-04",
                     "2.599875e-04",
                     "2.659875e-04",
                     "2.719875e-04",
                     "2.779875e-04",
                     "2.839875e-04",
                     "2.899875e-04",
                     "2.959875e-04",
                     "3.000000e-04"
                  ]
               },
               {
                  "data_name":"v1#branch",
                  "values":[
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "-2.56242e-06",
                     "-7.68724e-06",
                     "-1.79369e-05",
                     "-3.06713e-05",
                     "-5.61400e-05",
                     "-1.07077e-04",
                     "-2.08949e-04",
                     "-3.16527e-04",
                     "-4.84546e-04",
                     "-4.99975e-04",
                     "-4.99973e-04",
                     "-4.99968e-04",
                     "-4.99959e-04",
                     "-4.99940e-04",
                     "-4.99902e-04",
                     "-4.99827e-04",
                     "-4.99677e-04",
                     "-4.99380e-04",
                     "-4.99084e-04",
                     "-4.98791e-04",
                     "-4.98499e-04",
                     "-4.98208e-04",
                     "-4.97919e-04",
                     "-4.97631e-04",
                     "-4.97344e-04",
                     "-4.97059e-04",
                     "-4.96774e-04",
                     "-4.96491e-04",
                     "-4.96208e-04",
                     "-4.95927e-04",
                     "-4.95646e-04",
                     "-4.95366e-04",
                     "-4.95087e-04",
                     "-4.94808e-04",
                     "-4.94531e-04",
                     "-4.94254e-04",
                     "-4.93977e-04",
                     "-4.93702e-04",
                     "-4.93427e-04",
                     "-4.93152e-04",
                     "-4.92878e-04",
                     "-4.92604e-04",
                     "-4.92331e-04",
                     "-4.92058e-04",
                     "-4.91786e-04",
                     "-4.91514e-04",
                     "-4.91243e-04",
                     "-4.90972e-04",
                     "-4.90701e-04",
                     "-4.90431e-04",
                     "-4.90161e-04",
                     "-4.89891e-04",
                     "-4.89622e-04",
                     "-4.89353e-04",
                     "-4.89084e-04",
                     "-4.88815e-04",
                     "-4.88547e-04",
                     "-4.88279e-04",
                     "-4.88011e-04",
                     "-4.87744e-04",
                     "-4.87477e-04",
                     "-4.87210e-04",
                     "-4.86943e-04",
                     "-4.86677e-04",
                     "-4.86410e-04",
                     "-4.86232e-04"
                  ]
               }
            ]
         },
         {
            "key":"print_#2",
            "values":[
               {
                  "data_name":"time",
                  "values":[
                     "0.000000e+00",
                     "1.000000e-08",
                     "2.000000e-08",
                     "4.000000e-08",
                     "8.000000e-08",
                     "1.600000e-07",
                     "3.200000e-07",
                     "6.400000e-07",
                     "1.000000e-06",
                     "1.005125e-06",
                     "1.015374e-06",
                     "1.035874e-06",
                     "1.061343e-06",
                     "1.112281e-06",
                     "1.214156e-06",
                     "1.417908e-06",
                     "1.633075e-06",
                     "1.969139e-06",
                     "2.000000e-06",
                     "2.047146e-06",
                     "2.141437e-06",
                     "2.330020e-06",
                     "2.707185e-06",
                     "3.461515e-06",
                     "4.970176e-06",
                     "7.987498e-06",
                     "1.398750e-05",
                     "1.998750e-05",
                     "2.598750e-05",
                     "3.198750e-05",
                     "3.798750e-05",
                     "4.398750e-05",
                     "4.998750e-05",
                     "5.598750e-05",
                     "6.198750e-05",
                     "6.798750e-05",
                     "7.398750e-05",
                     "7.998750e-05",
                     "8.598750e-05",
                     "9.198750e-05",
                     "9.798750e-05",
                     "1.039875e-04",
                     "1.099875e-04",
                     "1.159875e-04",
                     "1.219875e-04",
                     "1.279875e-04",
                     "1.339875e-04",
                     "1.399875e-04",
                     "1.459875e-04",
                     "1.519875e-04",
                     "1.579875e-04",
                     "1.639875e-04",
                     "1.699875e-04",
                     "1.759875e-04",
                     "1.819875e-04",
                     "1.879875e-04",
                     "1.939875e-04",
                     "1.999875e-04",
                     "2.059875e-04",
                     "2.119875e-04",
                     "2.179875e-04",
                     "2.239875e-04",
                     "2.299875e-04",
                     "2.359875e-04",
                     "2.419875e-04",
                     "2.479875e-04",
                     "2.539875e-04",
                     "2.599875e-04",
                     "2.659875e-04",
                     "2.719875e-04",
                     "2.779875e-04",
                     "2.839875e-04",
                     "2.899875e-04",
                     "2.959875e-04",
                     "3.000000e-04"
                  ]
               },
               {
                  "data_name":"v1#branch",
                  "values":[
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "-2.56242e-06",
                     "-7.68724e-06",
                     "-1.79369e-05",
                     "-3.06713e-05",
                     "-5.61400e-05",
                     "-1.07077e-04",
                     "-2.08949e-04",
                     "-3.16527e-04",
                     "-4.84546e-04",
                     "-4.99975e-04",
                     "-4.99973e-04",
                     "-4.99968e-04",
                     "-4.99959e-04",
                     "-4.99940e-04",
                     "-4.99902e-04",
                     "-4.99827e-04",
                     "-4.99677e-04",
                     "-4.99380e-04",
                     "-4.99084e-04",
                     "-4.98791e-04",
                     "-4.98499e-04",
                     "-4.98208e-04",
                     "-4.97919e-04",
                     "-4.97631e-04",
                     "-4.97344e-04",
                     "-4.97059e-04",
                     "-4.96774e-04",
                     "-4.96491e-04",
                     "-4.96208e-04",
                     "-4.95927e-04",
                     "-4.95646e-04",
                     "-4.95366e-04",
                     "-4.95087e-04",
                     "-4.94808e-04",
                     "-4.94531e-04",
                     "-4.94254e-04",
                     "-4.93977e-04",
                     "-4.93702e-04",
                     "-4.93427e-04",
                     "-4.93152e-04",
                     "-4.92878e-04",
                     "-4.92604e-04",
                     "-4.92331e-04",
                     "-4.92058e-04",
                     "-4.91786e-04",
                     "-4.91514e-04",
                     "-4.91243e-04",
                     "-4.90972e-04",
                     "-4.90701e-04",
                     "-4.90431e-04",
                     "-4.90161e-04",
                     "-4.89891e-04",
                     "-4.89622e-04",
                     "-4.89353e-04",
                     "-4.89084e-04",
                     "-4.88815e-04",
                     "-4.88547e-04",
                     "-4.88279e-04",
                     "-4.88011e-04",
                     "-4.87744e-04",
                     "-4.87477e-04",
                     "-4.87210e-04",
                     "-4.86943e-04",
                     "-4.86677e-04",
                     "-4.86410e-04",
                     "-4.86232e-04"
                  ]
               },
               {
                  "data_name":"in",
                  "values":[
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "0.000000e+00",
                     "2.562416e-02",
                     "7.687249e-02",
                     "1.793691e-01",
                     "3.067137e-01",
                     "5.614029e-01",
                     "1.070781e+00",
                     "2.089538e+00",
                     "3.165373e+00",
                     "4.845694e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00",
                     "5.000000e+00"
                  ]
               }
            ]
         }
      ],
      "real":""
   }
```
</div>
</details>

#### SPECIFIC_PRINT
Parse the case, when the user prints only the data at a specific point. (such as v[t])

```json
{
   "type":"SPECIFIC_PRINT",
   "contents":[
      {
         "key":"print_#0",
         "values":[
            {
               "key":"time[k] ",
               "values":[
                  " 1.000000e-04"
               ]
            }
         ]
      }
   ],
   "real":""
}
```

#### DEBUG_MESSAGE
Display Debug Messages.(This data type is always assigned as the last value in the list(if debug=True or tag value is assigned)

```json
{
      "type":"DEBUG_MESSAGE",
      "contents":[
         {
            "key":"tag",
            "values":[
               "1bc29b36f623ba82aaf6724fd3b16718"
            ]
         },
         {
            "key":"time",
            "values":[
               0.025753021240234375
            ]
         }
      ],
      "real":""
   }
```

## Defined exception

### NgspiceNotFoundException

```json
{
   "type":"EXCEPTION",
   "contents":{
      "title":"NgspiceNotFoundException",
      "description":"You should install NGSPICE. If your NGSPICE is alrealdy installed, check the alias settings."
   },
   "real":""
}
```

### SomethingBadException

```json
{
   "type":"EXCEPTION",
   "contents":{
      "title":"SomethingBadException",
      "description":"A fatal error that can not be processed by the program has occurred."
   },
   "real":""
}
```

## Known Issues
1. User can't change Ngspice options.
2. Not available in version 3.6 or lower.
3. Not have all of the error logging and exception handling.
4. Can't cover all kinds of output.(feel free to report new data types)

## License

### Ngspice

```
******
** ngspice-34 : Circuit level simulation program
** The U. C. Berkeley CAD Group
** Copyright 1985-1994, Regents of the University of California.
** Copyright 2001-2020, The ngspice team.
** Please get your ngspice manual from http://ngspice.sourceforge.net/docs.html
** Please file your bug-reports at http://ngspice.sourceforge.net/bugrep.html
******
```

### ngspice-json-cli

MIT



