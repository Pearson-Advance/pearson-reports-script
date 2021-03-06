"""
Main module for additional proversity reports.
"""
from argparse import ArgumentParser
import os

from proversity_reports_script.request_report import FetchReportData


def main():
    """
    Main entry point of the script report generation.
    """
    parser = ArgumentParser()
    parser.add_argument(
        '--report',
        '-r',
        help='Get and upload the supported report.',
        required=True,
    )
    parser.add_argument('--config-file', '-c', help='Path to configuration file.', required=True)
    parser.add_argument('--oauth-config-file', help='Path to the Google oAuth configuration file.', required=True)
    parser.add_argument('--api-version', help='Version of the reports API.', default='v0')

    know_arguments, unknown_arguments = parser.parse_known_args()  # pylint: disable=unused-variable

    for unknown_argument in unknown_arguments:
        if unknown_argument.startswith(('-', '--')):
            parser.add_argument(unknown_argument)

    args = parser.parse_args()

    os.environ['CONFIGURATION_FILE_PATH'] = args.config_file
    os.environ['OAUTH_CONFIGURATION_FILE'] = args.oauth_config_file

    FetchReportData(
        report_name=args.report,
        extra_arguments=args,
        api_version=args.api_version,
    ).init_report_pipeline()


if __name__ == '__main__':
    main()
