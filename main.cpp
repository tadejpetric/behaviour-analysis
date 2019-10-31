
#include <astra/astra.hpp>
#include <chrono>
#include <iostream>

class BodyDisplay: public astra::FrameListener
{

    std::chrono::high_resolution_clock::time_point prev;
    float elapsed_milis{.0f};


    using BufferPtr = std::unique_ptr<uint8_t[]>;
    BufferPtr display_buffer{nullptr};

    int depth_width{0};
    int depth_height{0};

    using DepthPtr = std::unique_ptr<int16_t[]>;
    DepthPtr depth_data{nullptr};


public:
    virtual void on_frame_ready(astra::StreamReader& reader,
                                astra::Frame& frame) override
    {
        check_fps();

        print_bodies(frame); 
    }
    void check_fps() {
        const float fpsf = .2f;

        const auto now = std::chrono::high_resolution_clock::now();
        const float elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(now - prev).count();

        elapsed_milis = elapsed * fpsf + elapsed_milis * (1.f - fpsf);
        prev = now;

        const float fps = 1000.f / elapsed;

        std::cout << "### 0\n";
        std::cout << "fps " <<  fps << "\n";
        std::cout << "ms "<< ms << "\n";
        std::cout << "### 0\n";
    }

    void print_bodies(astra::Frame& frame) {
        std::cout << "--- 0\n";

        auto body_frame = frame.get<astra::BodyFrame>();
        const auto& bodies = body_frame.bodies();

        std::cout << "frame " << body_frame.frame_index() << "\n";
        std::cout << "people " << bodies.size() << "\n";

        for (const auto& body : bodies) {
            std::cout << "body_id " << static_cast<int>(body.id()) << "\n";
            const auto& all_joints = body.joints();

            for (const auto& joint : all_joints) {
                astra::JointType type = joint.type();
                /*
                 * JointType is an enum with the following values
                 0 Head
                 1 ShoulderSpine
                 2 LeftShoulder
                 3 LeftElbow
                 4 LeftHand
                 5 RightShoulder
                 6 RightElbow
                 7 RightHand
                 8 MidSpine
                 9 BaseSpine
                10 LeftHip
                11 LeftKnee
                12 LeftFoot
                13 RightHip
                14 RightKnee
                15 RightFoot
                16 LeftWrist
                17 RightWrist
                18 Neck
                19 Unknown
                */
                std::cout << "type " << static_cast<int>(type) << " ";
                auto pos = joint.world_position();
                std::cout << "x: " << pos.x << " y: " <<  pos.y << " z: " << pos.z;
                std::cout << "\n";
            }
        }
        std::cout << "---\n";
    }

};

astra::DepthStream configure_depth(astra::StreamReader& reader) {
    auto depthStream = reader.stream<astra::DepthStream>();
    astra::ImageStreamMode depthMode;

    depthMode.set_width(320);
    depthMode.set_height(240);
    depthMode.set_pixel_format(astra_pixel_formats::ASTRA_PIXEL_FORMAT_DEPTH_MM);
    depthMode.set_fps(30);

    depthStream.set_mode(depthMode);

    return depthStream;
}

int main(int argc, char** argv) {
    astra::initialize();

    const char* licenseString = "lol free demo";
    orbbec_body_tracking_set_license(licenseString);

    astra::StreamSet streamSet;
    astra::StreamReader reader = streamSet.create_reader();

    auto depthStream = configure_depth(reader);
    depthStream.start();

    auto body_stream = reader.stream<astra::BodyStream>();
    body_stream.start();
    BodyDisplay listener;
    reader.add_listener(listener);

    while (true) {
        astra_update();
    }

    astra::terminate();

    return 0;
}

