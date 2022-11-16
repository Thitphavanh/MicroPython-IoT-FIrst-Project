// ignore_for_file: public_member_api_docs, sort_constructors_first
import 'dart:convert';
import 'package:anitocorn_iot_app/models/sensor_model.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class SinglePage extends StatefulWidget {
  final String sensorCode;

  const SinglePage({
    Key? key,
    required this.sensorCode,
  }) : super(key: key);

  @override
  State<SinglePage> createState() => _SinglePageState();
}

class _SinglePageState extends State<SinglePage> {
  late String sensorCode;
  late Future<Sensor> sensorData;
  var baseUrl = Sensor.baseUrl;

  Future<Sensor> getSensorData() async {
    final url = Uri.http(baseUrl, '/sensor-current-single/$sensorCode');
    final response = await http.get(url);
    if (response.statusCode == 200) {
      return Sensor.fromJson(jsonDecode(utf8.decode(response.bodyBytes)));
    } else {
      throw Exception('Failed');
    }
  }

  @override
  void initState() {
    sensorCode = widget.sensorCode;
    sensorData = getSensorData();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        backgroundColor: Colors.transparent,
        foregroundColor: Colors.black,
        elevation: 0,
        title: Text('Single Data $sensorCode'),
      ),
      body: _singleData(),
    );
  }

  Widget _singleData() {
    return FutureBuilder(
      future: sensorData,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          return Column(
            children: [
              Text(
                'Sensor Code : ${snapshot.data!.code}',
                style: const TextStyle(fontSize: 20.0),
              ),
              Text(
                'Title Code : ${snapshot.data!.title}',
                style: const TextStyle(fontSize: 20.0),
              ),
              Text(
                'Temperature Code : ${snapshot.data!.temperature}',
                style: const TextStyle(fontSize: 20.0),
              ),
              Text(
                'Humidity Code : ${snapshot.data!.humidity}',
                style: const TextStyle(fontSize: 20.0),
              ),
              Text(
                'Timestamp Code : ${snapshot.data!.timestamp}',
                style: const TextStyle(fontSize: 20.0),
              ),
            ],
          );
        } else {
          return const Center(
            child: CircularProgressIndicator(),
          );
        }
      },
    );
  }
}
