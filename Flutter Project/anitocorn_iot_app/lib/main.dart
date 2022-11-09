import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';

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
  List sensorList = [];
  int _selectedIndex = 0;
  static const TextStyle optionStyle =
      TextStyle(fontSize: 30, fontWeight: FontWeight.bold);

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  Future<void> getSensorList() async {
    final Uri url = Uri.http('localhost:8000','/sensor-list/');
    final response = await http.get(url);
    if (response.statusCode == 200 && response.body.isNotEmpty) {
      final result = json.decode(response.body);

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
      censorSingleListTab(),
      const Text(
        'Index 0: Home',
        style: optionStyle,
      ),
      const Text(
        'Index 1: Business',
        style: optionStyle,
      ),
      const Text(
        'Index 2: School',
        style: optionStyle,
      ),
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

  Widget censorSingleListTab() {
    return ListView.builder(
      itemCount: sensorList.isEmpty ? 0 : sensorList.length,
      itemBuilder: (context, index) {
        return Card(
          child: ListTile(
            leading: Text('$sensorList[0]'),
          ),
        );
      },
    );
  }
}
