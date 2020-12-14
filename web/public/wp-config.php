<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'local' );

/** MySQL database username */
define( 'DB_USER', 'root' );

/** MySQL database password */
define( 'DB_PASSWORD', 'root' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'qx7GHr+XSeH6RnbDiR/UhX3FUqE2f5R4rQeqXDZ+2IWOW1zdzKLHSbMUdpTvPTCG1AheberQwOd2UiLGT8oIKg==');
define('SECURE_AUTH_KEY',  'dZ44XNG4da92zGGRxlJJ0avhUWYSoIOeoIrXnzFB/yM66L743GLh6g7Fti4cW6M02VRiMlPUHQZKXb5f14ui+w==');
define('LOGGED_IN_KEY',    'QHpdYF7Nh/9kd2gW/ag0h/fWYXtoXmeBHoK4gS5ClM0fL1VgTflK6GeMWJAkhfP+NuaDMaHZMecQzdeOXTVz9Q==');
define('NONCE_KEY',        'H7YiSzJK4/r978nrwrRrwr1pOKA6jwPX99J3YqvqQC1bLohilG2s1KGG+B+gudBQaZkeagsbTSNCyY1vx4kgmw==');
define('AUTH_SALT',        'iIQPpcuzXEQnPYKNO5/q9B7Ye18v137TL1mH6qqUFVnxsV9F2ZV8U0C0QtJtzHHLUNDSttW3vvN6Q4CPQihung==');
define('SECURE_AUTH_SALT', 'KRYNoLiagZ/jabKevz3OvqnMAjhn592m5wUxI1cehD9NrT+mLbT7d16waKN9feY8ZrSGPGk1EQq5/Kj9kbCGfQ==');
define('LOGGED_IN_SALT',   'hRxsjpkGtnz23ObYb/6nwZHPwg1yjS1tGLZsMXcHU+76KVtBRxMaIlxH5JSkZwi/a0lXejakwxvIuONmhk+ftg==');
define('NONCE_SALT',       'eD1EqaJ6UyY3WSCqfVluR9uaCOgu7vZY7P7CZz5+ZivVhoUtnpmq4ndklEX3f1yZbyyeS3DSkQ1JYruwiSy9cA==');

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';




/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', dirname( __FILE__ ) . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
