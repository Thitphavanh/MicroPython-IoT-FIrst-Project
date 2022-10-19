import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  String title = 'PHENOMENAL INC.';
  MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: title,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  TextEditingController sensorController = TextEditingController();
  TextEditingController tempController = TextEditingController();
  bool status = false;
  final dataList = <dynamic>[];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        foregroundColor: Colors.black,
        elevation: 0,
        centerTitle: true,
        title: const Text("PHENOMENAL INC."),
      ),
      body: Padding(
        padding: const EdgeInsets.symmetric(
          horizontal: 16.0,
          vertical: 16.0,
        ),
        child: Column(
          children: [
            buildImage(),
            const SizedBox(height: 16.0),
            buildSensorTextField(),
            const SizedBox(height: 16.0),
            buildTempTextField(),
            const SizedBox(height: 16.0),
            buildSwitch(),
            buildSubmitButton(),
            const SizedBox(height: 16.0),
            Text('VALUE : $dataList'),
            const SizedBox(height: 16.0),
            buildListView(),
          ],
        ),
      ),
    );
  }

  TextFormField buildSensorTextField() {
    return TextFormField(
      controller: sensorController,
      decoration: const InputDecoration(
        border: OutlineInputBorder(),
        hintText: 'ກະລຸນາໃສ່ຊື່ Sensor',
      ),
    );
  }

  TextFormField buildTempTextField() {
    return TextFormField(
      controller: tempController,
      decoration: const InputDecoration(
        border: OutlineInputBorder(),
        hintText: 'ກະລຸນາຕື່ມ Temp ເປັນ F',
      ),
      keyboardType: TextInputType.number,
    );
  }

  Row buildSwitch() {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text(
          'SENSOR STATUS',
          style: TextStyle(
            color: Colors.red[500],
          ),
        ),
        Switch(
          value: status,
          activeColor: Colors.red[500],
          onChanged: (value) {
            setState(() {
              status = value;
            });
          },
        ),
      ],
    );
  }

  buildImage() {
    return Image.asset(
      'assets/images/image.jpg',
      height: 150.0,
      width: Size.infinite.width,
      fit: BoxFit.cover,
    );
  }

  ElevatedButton buildSubmitButton() {
    return ElevatedButton.icon(
      style: ElevatedButton.styleFrom(
        fixedSize: const Size(160, 40),
        backgroundColor: Colors.redAccent,
      ),
      onPressed: () {
        if (sensorController.text.isNotEmpty &&
            tempController.text.isNotEmpty) {
          var celsius = (double.parse(tempController.text) - 32) / 9 * 5;
          var statusText = status ? 'ON' : 'OFF';

          setState(() {
            dataList.add([
              sensorController.text,
              celsius.toStringAsFixed(1),
              statusText
            ]);
          });
        }

        sensorController.text = '';
        tempController.text = '';
      },
      label: const Text('SUBMIT'),
      icon: const Icon(Icons.flutter_dash),
    );
  }

  Widget buildListView() {
    return Expanded(
      child: ListView.builder(
        itemCount: dataList.length,
        itemBuilder: (context, index) {
          return Card(
            child: ListTile(
              leading: Text('Pt : ${dataList[index][0]}'),
              title: Text('Temp : ${dataList[index][1]} °C'),
              trailing: Text('Status : ${dataList[index][2]}'),
            ),
          );
        },
      ),
    );
  }
}

// body: SingleChildScrollView(
//         child: Center(
//           child: Column(
//             mainAxisAlignment: MainAxisAlignment.start,
//             children: [
//               Padding(
//                 padding: const EdgeInsets.all(8.0),
//                 child: Image.asset(
//                   'assets/images/image.jpg',
//                   // 'https://cdn.dribbble.com/users/1622791/screenshots/11174104/flutter_intro.png',
//                   height: 300.0,
//                   width: Size.infinite.width,
//                   fit: BoxFit.cover,
//                 ),
//               ),
//               const SizedBox(height: 8.0),
//               const Text(
//                 'IoT Projects',
//                 style: TextStyle(
//                   color: Colors.black,
//                   fontSize: 18.0,
//                 ),
//               ),
//               Text(
//                 '$counter',
//                 style: Theme.of(context).textTheme.headline4,
//               ),
//               const SizedBox(height: 16.0),
//               TextField(
//                 controller: textController,
//                 decoration: const InputDecoration(
//                   border: OutlineInputBorder(),
//                 ),
//               ),
//               const SizedBox(height: 16.0),
//               ElevatedButton.icon(
//                 style: ElevatedButton.styleFrom(
//                   fixedSize: const Size(140, 40),
//                   backgroundColor: Colors.redAccent,
//                 ),
//                 onPressed: () {
//                   setState(() {
//                     message = textController.text;
//                   });
//                 },
//                 label: const Text('Enter'),
//                 icon: const Icon(Icons.flutter_dash),
//               ),
//               const SizedBox(height: 16.0),
//               Text(
//                 message,
//                 style: const TextStyle(
//                   color: Colors.black,
//                   fontSize: 18.0,
//                 ),
//               ),
//             ],
//           ),
//         ),
//       ),