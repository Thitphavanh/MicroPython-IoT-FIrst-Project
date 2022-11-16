// ignore_for_file: public_member_api_docs, sort_constructors_first
class Sensor {
  static String baseUrl = '192.168.163.1:8000';
  final String code;
  final String title;
  final String temperature;
  final String humidity;
  final String timestamp;

  Sensor({
    required this.code,
    required this.title,
    required this.temperature,
    required this.humidity,
    required this.timestamp,
  });

  factory Sensor.fromJson(Map<String, dynamic> json) {
    return Sensor(
      code: json['code'],
      title: json['title'],
      temperature: json['temperature'],
      humidity: json['humidity'],
      timestamp: json['timestamp'],
    );
  }
}
