# initicializa isso aq antes de qualquer outro script que possa chama ele
init -5 python:

    shader_vars = """
    uniform sampler2D tex0;
    uniform float u_time;
    uniform vec4 u_viewport;
    attribute vec2 a_tex_coord;
    varying vec2 v_tex_coord;

    uniform float u_frame;
    uniform float u_speed;
    uniform float u_distortion;
    uniform float u_distortion2;
    uniform float u_scale;
    uniform float u_scale2;
    uniform float u_static;
    uniform float u_vignette;
    uniform float u_interlacing;
    uniform float u_interlacing_y;
    uniform float u_debug;
    """
    perlin_functions = """
    #define NOISE Perlin
    float PerlinHash(vec2 st)
    {
        return fract(sin(dot(st.xy, vec2(12.9898, 78.233))) *
                        43758.5453123);
    }
    float Perlin(in vec2 st)
    {
        vec2 i = floor(st);
        vec2 f = fract(st);

        // Four corners in 2D of a tile
        float a = PerlinHash(i);
        float b = PerlinHash(i + vec2(1.0, 0.0));
        float c = PerlinHash(i + vec2(0.0, 1.0));
        float d = PerlinHash(i + vec2(1.0, 1.0));

        vec2 u = f * f * (3.0 - 2.0 * f);

        return mix(a, b, u.x) +
            (c - a) * u.y * (1.0 - u.x) +
            (d - b) * u.x * u.y;
    }
    """
    worley_functions = """
    #define NOISE Worley
    vec2 WorleyHash(vec2 p)
    {
        return fract(cos(p * mat2(-64.2, 71.3, 81.4, -29.8)) * 8321.3);
    }
    float Worley(vec2 p)
    {
        float dist = 1.;
        vec2 I = floor(p);
        vec2 F = fract(p);

        for (int x = -1; x <= 1; x++)
        {
            for (int y = -1; y <= 1; y++)
            {
                float D = distance(WorleyHash(I + vec2(x, y)) + vec2(x, y), F);
                dist = min(dist, D);
            }
        }
        return dist;
    }
    """
    fragment_functions = """
    vec2 Noise2D(vec2 uv, float time)
    {
        vec2 q = vec2(0.);
        q.x = NOISE(uv + time);
        q.y = NOISE(uv + 1.);
        vec2 r = vec2(0.);
        r.x = NOISE(uv + q + vec2(1.7, 9.2) + 0.15 * time);
        r.y = NOISE(uv + q + vec2(8.3, 2.8) + 0.126 * time);
        return clamp(r, 0., 1.);
    }
    float BoxSDF(vec2 p, vec2 scale)
    {
        vec2 dist = abs(p) - scale;
        return length(max(dist, 0.)) + min(max(dist.x, dist.y), 0.);
    }
    """
    fragment_shader = """
    float _NoiseThresh = 0.5;
    float _NoiseSmooth = 0.;

    // make texture coordinates between 0 and 1
    vec2 uv = v_tex_coord.st;

    vec2 centerUV = uv - 0.5; // puts 0,0 in the center
    // create a mask for the edges of the image so that
    // distortion doesn't cause weird artifacting
    float mask = BoxSDF(centerUV, vec2(0.5, 0.5));
    mask = clamp(smoothstep(-0.01, 0.11, 0.0001 - mask), 0., 1.);

    // set frame rate
    float frame = floor(u_time * (24. / u_frame));

    // get distortion
    vec2 fbm = Noise2D(uv * u_scale, frame * u_speed);
    fbm = smoothstep(_NoiseThresh - _NoiseSmooth, _NoiseThresh + _NoiseSmooth, fbm);

    // make the noise value between -1 and 1 rather than 0 and 1 to allow
    // uvs to be distorted in either direction
    fbm = fbm * 2. - 1.;
    // mask out the edges
    fbm *= mask;

    // secondary distortion
    vec2 secondary = Noise2D(uv * u_scale2, frame * u_speed);
    secondary = mod(frame, 2.) == 0.? secondary : 1. - secondary;
    secondary *= mask;
    secondary = secondary * 2. - 1.;

    // offset texture coordinates based on distortion
    vec2 distortedUV = uv + fbm * u_distortion + secondary * u_distortion2;

    // interlacing (line wiggle)
    distortedUV.x -= (sin(distortedUV.y * u_interlacing_y + frame) * 0.5 + 0.5) * 
        u_interlacing * mask;

    // sample texture with distorted UVs
    vec4 col = texture2D(tex0, distortedUV, 0.);

    // static
    vec2 texel = 1. / u_viewport.pq;
    float n = fract(cos(
        (sin(centerUV.x / texel.x) * centerUV.y / texel.y + frame * 0.01)
        * 90.) * 343.);
    col.rgb = mix(col.rgb, min(col.rgb, n), u_static);
    vec3 debugColor = vec3(fbm.x * 0.5 + 0.5, fbm.y * 0.5 + 0.5, 1.);
    col.rgb *= mix(vec3(1.), debugColor, u_debug);

    // nice little vignette effect
    float vignette = 1. - dot(centerUV, centerUV) * u_vignette;
    col.rgb *= vignette;

    gl_FragColor = col;
    """

    renpy.register_shader(
        "distortion_perlin",
        variables=shader_vars,
        vertex_functions="",
        fragment_functions=str(perlin_functions + fragment_functions),
        vertex_200="",
        fragment_200=fragment_shader)

    renpy.register_shader(
        "distortion_worley",
        variables=shader_vars,
        vertex_functions="",
        fragment_functions=str(worley_functions + fragment_functions),
        vertex_200="",
        fragment_200=fragment_shader)