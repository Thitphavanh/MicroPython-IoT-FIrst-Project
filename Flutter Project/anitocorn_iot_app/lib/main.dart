import 'dart:convert';

import 'package:anitocorn_iot_app/models/sensor_model.dart';
import 'package:anitocorn_iot_app/pages/home_page.dart';
import 'package:anitocorn_iot_app/pages/single_page.dart';
import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';

import 'pages/multi_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Anitocorn IoT',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Smart IoT'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  static const TextStyle optionStyle =
      TextStyle(fontSize: 30, fontWeight: FontWeight.bold);
  List sensorList = [];
  int _selectedIndex = 0;
  var baseUrl = Sensor.baseUrl;
  TextEditingController searchController = TextEditingController();
  bool runState = false;

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  Future<List<Sensor>> searchDataTable() async {
    List<Sensor> sensorMulti = [];
    List<Sensor> sensorFromJson(String body) =>
        List<Sensor>.from(jsonDecode(body).map((x) => Sensor.fromJson(x)));

    final url =
        Uri.http(baseUrl, '/sensor-current-multiple/${searchController.text}');
    final response = await http.get(url);

    if (response.statusCode == 200) {
      var responseBody = sensorFromJson(utf8.decode(response.bodyBytes));

      for (var item in responseBody) {
        sensorMulti.add(item);
      }
    } else {
      throw Exception('Failed');
    }
    return sensorMulti;
  }

  Future<void> getSensorList() async {
    var url = Uri.http(baseUrl, '/sensor-list');
    var response = await http.get(url);
    if (response.statusCode == 200 && response.body.isNotEmpty) {
      // var result = json.decode(response.body);
      var result = utf8.decode(response.bodyBytes);

      setState(() {
        sensorList = jsonDecode(result);
      });
    }
  }

  @override
  void initState() {
    getSensorList();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    List<Widget> _widgetOptions = <Widget>[
      const HomePage(),
      sensorSingleListTab(),
      sensorMultiListTab(),
      searchFormTab(),
    ];
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        backgroundColor: Colors.transparent,
        foregroundColor: Colors.black,
        elevation: 0,
        title: const Text('Smart Home'),
      ),
      body: Center(
        child: _widgetOptions.elementAt(_selectedIndex),
      ),
      bottomNavigationBar: BottomNavigationBar(
        backgroundColor: Colors.transparent,
        unselectedItemColor: Colors.black38,
        selectedItemColor: Colors.black,
        showUnselectedLabels: true,
        elevation: 0,
        currentIndex: _selectedIndex,
        onTap: _onItemTapped,
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'HOME',
            // backgroundColor: Colors.black,
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.data_object),
            label: 'SINGLE',
            // backgroundColor: Colors.black,
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.data_array),
            label: 'MULTI',
            // backgroundColor: Colors.black,
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.youtube_searched_for),
            label: 'SEARCH',
            // backgroundColor: Colors.black,
          ),
        ],
      ),
    );
  }

  Widget sensorSingleListTab() {
    return ListView.builder(
      itemCount: sensorList.isEmpty ? 0 : sensorList.length,
      itemBuilder: (context, index) {
        return Card(
          child: ListTile(
            leading: Text(sensorList[index]),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => SinglePage(
                    sensorCode: sensorList[index],
                  ),
                ),
              );
            },
          ),
        );
      },
    );
  }

  Widget sensorMultiListTab() {
    return ListView.builder(
      itemCount: sensorList.isEmpty ? 0 : sensorList.length,
      itemBuilder: (context, index) {
        return Card(
          child: ListTile(
            leading: Text(sensorList[index]),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => MultiPage(
                    sensorCode: sensorList[index],
                  ),
                ),
              );
            },
          ),
        );
      },
    );
  }

  Widget searchFormTab() {
    return Column(
      children: [
        TextFormField(
          controller: searchController,
          decoration: const InputDecoration(
              border: OutlineInputBorder(),
              hintText: 'Please entry name sensor'),
        ),
        ElevatedButton(
          onPressed: () {
            if (searchController.text.isNotEmpty) {
              setState(() {
                runState = true;
                searchFormTab();
              });
            }
          },
          child: const Text('SEARCH'),
        ),
        runState ? _searchDataTable() : Container()
      ],
    );
  }

  Widget _searchDataTable() {
    return Expanded(
      child: FutureBuilder(
        future: searchDataTable(),
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return SingleChildScrollView(
              child: DataTable(
                columns: const <DataColumn>[
                  DataColumn(
                    label: Expanded(
                      child: Text(
                        'Code',
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                    ),
                  ),
                  DataColumn(
                    label: Expanded(
                      child: Text(
                        'Title',
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                    ),
                  ),
                  DataColumn(
                    label: Expanded(
                      child: Text(
                        'Temp',
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                    ),
                  ),
                  DataColumn(
                    label: Expanded(
                      child: Text(
                        'Humid',
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                    ),
                  ),
                  DataColumn(
                    label: Expanded(
                      child: Text(
                        'Timestamp',
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                    ),
                  ),
                ],
                rows: snapshot.data!
                    .map(
                      (e) => DataRow(cells: [
                        DataCell(Text(e.code)),
                        DataCell(Text(e.title)),
                        DataCell(Text(e.temperature)),
                        DataCell(Text(e.humidity)),
                        DataCell(Text(e.timestamp)),
                      ]),
                    )
                    .toList(),
              ),
            );
          } else {
            return const Center(
              child: CircularProgressIndicator(),
            );
          }
        },
      ),
    );
  }
}
