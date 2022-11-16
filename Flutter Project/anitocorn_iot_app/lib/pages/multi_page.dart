// ignore_for_file: public_member_api_docs, sort_constructors_first
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import '../models/sensor_model.dart';

class MultiPage extends StatefulWidget {
  final String sensorCode;
  const MultiPage({
    Key? key,
    required this.sensorCode,
  }) : super(key: key);

  @override
  State<MultiPage> createState() => _MultiPageState();
}

class _MultiPageState extends State<MultiPage> {
  late String sensorCode;
  var baseUrl = Sensor.baseUrl;

  Future<List<Sensor>> getSensorData() async {
    List<Sensor> sensorMulti = [];
    List<Sensor> sensorFromJson(String body) =>
        List<Sensor>.from(jsonDecode(body).map((x) => Sensor.fromJson(x)));

    final url = Uri.http(baseUrl, '/sensor-current-multiple/$sensorCode');
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

  @override
  void initState() {
    sensorCode = widget.sensorCode;
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
        title: Text('Multi Data $sensorCode'),
      ),
      body: _multiData(),
    );
  }

  Widget _multiData() {
    return FutureBuilder(
      future: getSensorData(),
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
    );
  }
}
