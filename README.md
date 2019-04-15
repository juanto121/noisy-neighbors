# Noisy Neighbors
This project contains scripts and configurations used for measuring, recording, publishing logs and audios
of noise levels.

# System design
The following is a description of the system. This repo contains the relevant files for the raspberry.
```
  +----------------------------------------------------+
  |                                                    |
  |    raspberry                                       |
  |                                                    |
  |                                                    |           +----------------------+
  |                                                    |           |Measurements DB       |
  | +------------+  +-------------+  +--------------+  |           |(Influxdb)            |
  | |main.py     |  |soundmeter   |  |fluentbit     +------------> |                      |
  | |            |  |             |  |              |  |           |                      |
  | +---+--------+  +-------------+  +--------------+  |           |                      |
  |     |                                              |           +----+-----------+-----+
  +----------------------------------------------------+                ^           ^
        |                                                               |           |
        |                                                               |           |
        |                                                               |           |
        |                                                               |           |
        v                                                          +----+----+    +-+---------------+      +-------------------------+
  +-----+--------+                                                 | Grafana |    |noisyneighbor.co <------+noisyneighbor.co(Angular)|
  |Recordings    |                                                 |         |    |API              |      +-------------------------+
  |S3-bucket     |                                                 +---------+    |                 |
  +-----+--------+                                                                | +------------+  |
        |                                                                         | |db queries  |  |
        |                                                                         | +------------+  |
        v                                                                         |                 |
  +-----+--------+        +-----------------------+                               | +------------+  |
  |AWS           +------->+Python                 <---------------------------------+recordings  |  |
  |Lambda trigger|        |Sound classifier (api) |                               | +------------+  |
  +--------------+        +--+--------------------+                               |                 |
                             |                                                    |                 |
                          +--v-------+                                            |                 |
                          |MONGO-DB  |                                            |                 |
                          |Classifier|                                            +-----------------+
                          +----------+

```